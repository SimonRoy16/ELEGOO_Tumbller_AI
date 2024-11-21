#include <stdint.h>

uint8_t loopCounter = 0;

void setup() {
  // put your setup code here, to run once:
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(13, OUTPUT);
}

void loop() {
  analogWrite(5, loopCounter);
  analogWrite(9, UINT8_MAX - loopCounter);

  // Toggle STBY pin
  if ((loopCounter % 10) == 0) {
    digitalWrite(13, LOW);
  } else {
    digitalWrite(13, HIGH);
  }

  // Toggle spin direction
  if (loopCounter > 128) {
    digitalWrite(2, LOW);
    digitalWrite(3, HIGH);
    digitalWrite(6, LOW);
    digitalWrite(7, HIGH);
  } else {
    digitalWrite(2, HIGH);
    digitalWrite(3, LOW);
    digitalWrite(6, HIGH);
    digitalWrite(7, LOW);
  }
  delay(10);
  loopCounter++;
}
