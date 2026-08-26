#include "Motor.h"

// =============================================
// 모터별 상태 변수 (4개 모터)
// =============================================
static volatile int _speed1 = 0,  _state1a = LOW,  _state1b = LOW;
static volatile int _speed2 = 0,  _state2a = LOW,  _state2b = LOW;
static volatile int _speed3 = 0,  _state3a = LOW,  _state3b = LOW;
static volatile int _speed4 = 0,  _state4a = LOW,  _state4b = LOW;

// PWM 카운터 (0~19 반복, 20단계)
static volatile int  _counter      = 0;
static          bool _timerStarted = false;

// =============================================
// 서보 카운터 (0~199 반복)
// 200 × 0.1ms = 20ms = 50Hz (서보 표준 주기)
// angle 0   → 10카운트 (1ms  = 0°  위치)
// angle 90  → 15카운트 (1.5ms = 90° 위치)
// angle 180 → 20카운트 (2ms  = 180°위치)
// pulse = 0  → 토크 오프 (신호 없음)
// =============================================
static volatile int _servoCounter = 0;
static volatile int _servo1Pulse  = 0;  // ISR 카운트 단위 (0 = 오프)
static volatile int _servo2Pulse  = 0;

// 좌우 모터 번호
static int g_leftMotor  = 2;
static int g_rightMotor = 3;

// 좌우 모터 방향 부호
// g_leftSign  = -1 : 좌측 모터 역방향 보정 (물리적 장착 방향)
// g_rightSign =  1 : 우측 모터 정방향
static int g_leftSign  = -1;
static int g_rightSign =  1;

// 스톱워치 기준값 (millis 단위)
static unsigned long _timerStart = 0;

// =============================================
// Timer1 인터럽트 (0.1ms마다 실행)
// 16MHz / 8 / 200 = 10,000Hz → 0.1ms 주기
// 0.1ms × 20단계 = 2ms = 500Hz PWM
// =============================================
ISR(TIMER1_COMPA_vect)
{
  // 모터 1
  if (_counter < _speed1) { digitalWrite(MOTOR1_PIN1, _state1a); digitalWrite(MOTOR1_PIN2, _state1b); }
  else                     { digitalWrite(MOTOR1_PIN1, LOW);      digitalWrite(MOTOR1_PIN2, LOW);      }

  // 모터 2
  if (_counter < _speed2) { digitalWrite(MOTOR2_PIN1, _state2a); digitalWrite(MOTOR2_PIN2, _state2b); }
  else                     { digitalWrite(MOTOR2_PIN1, LOW);      digitalWrite(MOTOR2_PIN2, LOW);      }

  // 모터 3
  if (_counter < _speed3) { digitalWrite(MOTOR3_PIN1, _state3a); digitalWrite(MOTOR3_PIN2, _state3b); }
  else                     { digitalWrite(MOTOR3_PIN1, LOW);      digitalWrite(MOTOR3_PIN2, LOW);      }

  // 모터 4
  if (_counter < _speed4) { digitalWrite(MOTOR4_PIN1, _state4a); digitalWrite(MOTOR4_PIN2, _state4b); }
  else                     { digitalWrite(MOTOR4_PIN1, LOW);      digitalWrite(MOTOR4_PIN2, LOW);      }

  // 카운터 0~19 반복 (20단계)
  if (++_counter >= 20) _counter = 0;

  // 서보 PWM (0~199 반복, 50Hz)
  if (_servo1Pulse > 0)
    digitalWrite(SERVO1_PIN, (_servoCounter < _servo1Pulse) ? HIGH : LOW);
  if (_servo2Pulse > 0)
    digitalWrite(SERVO2_PIN, (_servoCounter < _servo2Pulse) ? HIGH : LOW);
  if (++_servoCounter >= 200) _servoCounter = 0;
}

// =============================================
// PWM 타이머 설정 (내부 전용)
// Timer1 CTC 모드, 분주비 8, OCR1A=199 → 0.1ms
// =============================================
static void startTimer()
{
  if (_timerStarted) return;         // 이미 시작했으면 건너뜀

  TCCR1A = 0;                        // 일반 모드 초기화
  TCCR1B = (1 << WGM12) | (1 << CS11); // CTC 모드, 분주비 8
  OCR1A  = 199;                      // 0.1ms 주기
  TIMSK1 = (1 << OCIE1A);           // 인터럽트 활성화
  sei();                             // 전역 인터럽트 허용

  _timerStarted = true;
}

// =============================================
// 내부 헬퍼: 모터 핀 OUTPUT 설정
// =============================================
static void initMotorPins(int motorNum)
{
  switch (motorNum) {
    case 1: pinMode(MOTOR1_PIN1, OUTPUT); pinMode(MOTOR1_PIN2, OUTPUT); break;
    case 2: pinMode(MOTOR2_PIN1, OUTPUT); pinMode(MOTOR2_PIN2, OUTPUT); break;
    case 3: pinMode(MOTOR3_PIN1, OUTPUT); pinMode(MOTOR3_PIN2, OUTPUT); break;
    case 4: pinMode(MOTOR4_PIN1, OUTPUT); pinMode(MOTOR4_PIN2, OUTPUT); break;
  }
}

// =============================================
// 내부 헬퍼: 부호 있는 파워로 모터 방향 결정
// power: -20 ~ 20
//   power > 0 → CW  (첫 번째 핀 HIGH)
//   power < 0 → CCW (두 번째 핀 HIGH)
//   power = 0 → 정지
// =============================================
static void setMotorPower(int motorNum, int power)
{
  power = constrain(power, -20, 20);
  int spd = abs(power);

  switch (motorNum) {
    case 1:
      _speed1  = spd;
      _state1a = (power > 0) ? HIGH : LOW;
      _state1b = (power < 0) ? HIGH : LOW;
      break;
    case 2:
      _speed2  = spd;
      _state2a = (power > 0) ? HIGH : LOW;
      _state2b = (power < 0) ? HIGH : LOW;
      break;
    case 3:
      _speed3  = spd;
      _state3a = (power > 0) ? HIGH : LOW;
      _state3b = (power < 0) ? HIGH : LOW;
      break;
    case 4:
      _speed4  = spd;
      _state4a = (power > 0) ? HIGH : LOW;
      _state4b = (power < 0) ? HIGH : LOW;
      break;
  }
}

// =============================================
// 공개 API 구현
// =============================================

// 모터 초기화 (좌우 모터 번호 등록 + 타이머 시작)
void motorBegin(int leftMotor, int rightMotor)
{
  g_leftMotor  = leftMotor;
  g_rightMotor = rightMotor;

  initMotorPins(g_leftMotor);
  initMotorPins(g_rightMotor);

  pinMode(SERVO1_PIN, OUTPUT);
  pinMode(SERVO2_PIN, OUTPUT);

  startTimer();
}

// 스톱워치 타이머 초기화 (timer(0) 호출 시 리셋)
void timer(int reset)
{
  if (reset == 0) _timerStart = millis();
}

// 경과 시간 반환 (ms 단위)
unsigned int timer_read()
{
  return (unsigned int)(millis() - _timerStart);
}

// 차륜 제어
// leftpower: -20 ~ 20  , rightpower : -16 ~ 16
// 내부적으로 모터 장착 방향(g_leftSign, g_rightSign) 보정 적용
// g_rightTrim: 오른쪽 모터 속도 보정 (절댓값 기준, 음수=감속) -> 모터 성능때문에 현재 테스트한 두 모터에서는 오른쪽 모터가 속도가 더 빨라 4단계 정도 절대 감속함. 
static int g_rightTrim = 0 ;  // 오른쪽 모터 4단계 감속

void wheel(int leftpower, int rightpower)
{
  if      (rightpower > 0) rightpower = max(0,   rightpower + g_rightTrim);
  else if (rightpower < 0) rightpower = min(0,   rightpower - g_rightTrim);

  setMotorPower(g_leftMotor,  leftpower  * g_leftSign);
  setMotorPower(g_rightMotor, rightpower * g_rightSign);
}

// 서보 제어 (angle: 0=토크오프, 1~180=각도)
// map(angle, 0, 180, 10, 20) → ISR 카운트 단위 (0.1ms × 카운트 = 펄스폭)
void servo1(int angle)
{
  if (angle == 0) { _servo1Pulse = 0; digitalWrite(SERVO1_PIN, LOW); return; }
  _servo1Pulse = map(constrain(angle, 1, 180), 0, 180, 10, 20);
}

void servo2(int angle)
{
  if (angle == 0) { _servo2Pulse = 0; digitalWrite(SERVO2_PIN, LOW); return; }
  _servo2Pulse = map(constrain(angle, 1, 180), 0, 180, 10, 20);
}
