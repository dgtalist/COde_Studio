#include "Drive.h"

const int Select_Button_Pin = 4;

void setup() {
  pinMode(Select_Button_Pin, INPUT_PULLUP);
  motorBegin(1,3);
  bool isSwitchPressed = !digitalRead(Select_Button_Pin);
  while (digitalRead(Select_Button_Pin) == HIGH) {
  }
  LIFT_UP(1);
  delay(2000);
  LIFT_DOWN(1);
  delay(2000);
}

void loop() {
  FF(0,3,20,200);
  LEFT(-17,17);
  FF(0,2,20,100);



  // LIFT_DOWN(1);
  // RIGHT(17, -17);
  // RIGHT(17, -17);
  // FF(0,3,20,100);
  // delay(500);
  // FF(0,1,20,100);

  // LEFT(-20,20);
  // FF(0,2,20,0);

  while(true);
}
