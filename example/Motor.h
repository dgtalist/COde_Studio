#ifndef MOTOR_API_H
#define MOTOR_API_H

#include <Arduino.h>
#include <avr/interrupt.h>

// =============================================
// 모터 핀 설정 
// =============================================
#define MOTOR1_PIN1  5
#define MOTOR1_PIN2  6
#define MOTOR2_PIN1  12
#define MOTOR2_PIN2  13
#define MOTOR3_PIN1  8
#define MOTOR3_PIN2  9
#define MOTOR4_PIN1  10
#define MOTOR4_PIN2  11

// =============================================
// 서보 핀 설정 (A4, A5)
// =============================================
#define SERVO1_PIN   A4
#define SERVO2_PIN   A5

// =============================================
// 모터 초기화
// leftMotor, rightMotor: 1~4 (모터 번호)
// setup()에서 한 번만 호출
// =============================================
void motorBegin(int leftMotor, int rightMotor);

// =============================================
// timer(0) : 타이머 초기화 (시작)
// timer_read() : 경과 시간 반환 (ms 단위)
// =============================================
void timer(int reset);
unsigned int timer_read();

// =============================================
// 차륜 제어
// leftpower, rightpower: -20 ~ 20
//   양수 = 전진 방향
//   음수 = 후진 방향
//   0    = 정지
// =============================================
void wheel(int leftpower, int rightpower);

// =============================================
// 서보 모터 제어
// angle: 0~180 (각도)
//   0    = 토크 오프 (신호 없음)
//   1~180 = 해당 각도로 이동
// servo1 → A4, servo2 → A5
// =============================================
void servo1(int angle);
void servo2(int angle);

#endif
