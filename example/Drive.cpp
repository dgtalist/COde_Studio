#include "Drive.h"

unsigned char i = 0;	//반복문 변수

void FF(unsigned char acc, unsigned char count, char speed, unsigned int f_delay)	//전진 라인트레이서 : 1. 초기 가속도 시간값 (0~255) 2. 직진횟수 (0~255) 3. 속도 (0~20) 4. 직진딜레이값 (0~65535)
{
    for(i=2;i<=speed;i++)	//모터시작속도 2부터 speed값 만큼 반복
    {
        LINETRACER(i);	//라인트레이서 함수에 i값 대입
        delay(acc);	//가속도 시간값 만큼 딜레이
    }
    wheel(speed,speed);	//양쪽 모터 전진
    for(i=0;i<count;i++)	//직진 횟수 만큼 반복
    {
        while(1)	//무한 반복
        {
            LINETRACER(speed);	//라인트레이서 함수에 속도 대입
            if((CB1&&CB2)||(CB3&&CB4))	//1번센서 검정색, 4번센서 검정색일 때
            {
                break;	//반복 빠져나옴
            }
        }
        while(1)	//무한 반복
        {
            LINETRACER(speed);	//라인트레이서 함수에 속도 대입
            if(CW1&&CW4)	//1번센서 흰색, 4번센서 흰색일 때
            {
                break;	//반복 빠져나옴
            }
        }
    }
    if(f_delay!=0)	//직진딜레이 값이 있는 경우
    {
        timer(0);	//타이머 초기화
        wheel(speed,speed);	//양쪽 모터 전진
        while(1)
        {
            LINETRACER(speed);	//라인트레이서 함수에 속도 대입
            if(timer_read()>f_delay)	//직진딜레이값 만큼 시간이 지나면
            {
                break;	//반복 빠져나옴
            }
        }
    }
    wheel(0,0);	//모터 정지
}
void LINETRACER(char speed)	//라인트레이서 함수 : 1. 속도(0~20)
{
    if(LW2&&LW3)
    {
        wheel(speed,speed);	//왼쪽 모터와 오른쪽 모터 모두 직진
    }
    else if(LB2&&LW3)	//2번센서 검정색, 3번센서가 흰색일때
    {
        wheel(speed-(speed/1.5),speed);	//왼쪽 모터 감속, 오른쪽 모터 직진
    }
    else if(LW2&&LB3)	//2번센서가 흰색, 3번센서가 검정색일때
    {
        wheel(speed,speed-(speed/1.5));	//왼쪽 모터 직진, 오른쪽 모터 감속
    }
    else if(LB2&&LB3)	//2번센서 검정색, 3번센서가 검정색일때
    {
        wheel(speed,speed);	//왼쪽 모터와 오른쪽 모터 모두 직진
    }
}
void LEFT(char lspeed, char rspeed)	//좌회전 함수 : 1. 직진딜레이값(0~65535) 2. 속도(0~20)
{
    wheel(lspeed,rspeed);
    while(1)	//무한반복
    {
        if(CB1)	//4번센서가 검정색에 닿으면
        {
            break;	//무한반복 빠져나옴
        }
    }
    while(1)	//무한반복
    {
        if(CW1)	//4번센서가 흰색에 닿으면
        {
            break;	//무한반복 빠져나옴
        }
    }
    while(1)	//무한반복
    {
        if(CB2)	//3번센서가 검정색에 닿으면
        {
            break;	//무한반복
        }
    }
    wheel(0,0);	//모터정지
}
void RIGHT(char lspeed, char rspeed)	//우회전 함수 : 1. 직진딜레이값 (0~65535) 2. 속도 (0~20)
{
    wheel(lspeed,rspeed);
    while(1)	//무한반복
    {
        if(CB4)	//1번센서가 검정색에 닿으면
        {
            break;	//무한반복 빠져나옴
        }
    }
    while(1)	//무한반복
    {
        if(CW4)	//1번센서가 흰색에 닿으면
        {
            break;	//무한반복 빠져나옴
        }
    }
    while(1)	//무한반복
    {
        if(CB3)	//2번센서가 검정색에 닿으면
        {
            break;	//무한반복 빠져나옴
        }
    }
    wheel(0,0);	//모터정지
}
void LINE_DELAY(unsigned int _delay,char speed)	//시간만큼 라인트레이싱 1. 동작시간(0~65535) 2. 속도(0~20)
{
    timer(0);	//타이머 초기화
    wheel(speed,speed);	//양쪽 모터 직진
    while(1)	//무한반복
    {
        LINETRACER(speed);	//라인트레이서 함수 속도 대입
        if(timer_read()>_delay)	//직진딜레이값 만큼 시간이 지나면
        {
            break;	//무한 반복 빠져나옴
        }
    }
    wheel(0,0);	//모터정지
}
void LIFT_DOWN(unsigned char _delay)	//팔레트 아래로 내이기 1. 속도(0~255)
{
    for(i=UP;i>DOWN;i--)	//팔레트 올린 위치부터 내리는 위치까지 반복
    {
        servo1(i);	//서모모터 i값 대입
        delay(_delay);	//내리는 속도
    }
    servo1(DOWN);	//팔레트 아래로 내리기
    delay(100);	//0.1초 유지
    servo1(0);	//서보 토크 오프
}
void LIFT_UP(unsigned char _delay)	//팔레트 위로 올리기 1. 속도(0~255)
{
    for(i=DOWN;i<UP;i++)	//팔레트 내린 위치부터 올리는 위치까지 반복
    {
        servo1(i);	//서보모터 i값 대입
        delay(_delay);	//올리는 속도
    }
    servo1(UP);	//팔레트 위로 올리기
    delay(100);	//0.1초 유지
}
