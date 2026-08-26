#ifndef DRIVE_H
#define DRIVE_H

#include "Motor.h"

#define LINE_WHITE 200	//라인트레이서 흰색 값
#define LINE_BLACK 500	//라인트레이서 검정색 값
#define CROSS_WHITE 200	//크로스 흰색 값
#define CROSS_BLACK 500	//크로스 검정색 값
#define UP 170	//팔레트 서보 위로 올리는 값
#define DOWN 30	//팔레트 서보 아래로 내리는 값

#define CW1 (analogRead(A0)<=CROSS_WHITE)	//1번센서 크로스 흰색값
#define CW2 (analogRead(A1)<=CROSS_WHITE)	//2번센서 크로스 흰색값
#define CW3 (analogRead(A2)<=CROSS_WHITE)	//3번센서 크로스 흰색값
#define CW4 (analogRead(A3)<=CROSS_WHITE)	//4번센서 크로스 흰색값
#define CB1 (analogRead(A0)>CROSS_BLACK)	//1번센서 크로스 검정값
#define CB2 (analogRead(A1)>CROSS_BLACK)	//2번센서 크로스 검정값
#define CB3 (analogRead(A2)>CROSS_BLACK)	//3번센서 크로스 검정값
#define CB4 (analogRead(A3)>CROSS_BLACK)	//4번센서 크로스 검정값
#define LW1 (analogRead(A0)<LINE_WHITE)	//1번센서 라인 흰색값
#define LW2 (analogRead(A1)<LINE_WHITE)	//2번센서 라인 흰색값
#define LW3 (analogRead(A2)<LINE_WHITE)	//3번센서 라인 흰색값
#define LW4 (analogRead(A3)<LINE_WHITE)	//4번센서 라인 흰색값
#define LB1 (analogRead(A0)>LINE_BLACK)	//1번센서 라인 검정값
#define LB2 (analogRead(A1)>LINE_BLACK)	//2번센서 라인 검정값
#define LB3 (analogRead(A2)>LINE_BLACK)	//3번센서 라인 검정값
#define LB4 (analogRead(A3)>LINE_BLACK)	//4번센서 라인 검정값

extern unsigned char i;	//반복문 변수

void LINETRACER(char speed);
void LEFT(char lspeed, char rspeed);
void LEFT2(char lspeed, char rspeed);
void RIGHT(char lspeed, char rspeed);
void FF(unsigned char acc, unsigned char count, char speed, unsigned int f_delay);
void LIFT_UP(unsigned char _delay);
void LIFT_DOWN(unsigned char _delay);
void LINE_DELAY(unsigned int _delay,char speed);

#endif
