#line 2 "basic.ino"

#include <AUnit.h>

test(correct) {
  int x = 1;
  assertEqual(x, 1);
}

test(incorrect) {
  int x = 1;
  assertNotEqual(x, 1);
}

//----------------------------------------------------------------------------
// setup() and loop()
//----------------------------------------------------------------------------

void setup() {
  Serial.begin(115200);
}

void loop() {
  aunit::TestRunner::run();
}
