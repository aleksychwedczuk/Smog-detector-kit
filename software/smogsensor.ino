//Very simple code - all we need to do is read the light level on one single pin.
//Set READ_PIN to the pin that is used in Your hardware as the light level pin.

#define READ_PIN A0

void setup() {
  Serial.begin(9600); //init the serial - !9600 is the rate for Python 3 code too!

  Serial.print("[CTR] All systems operational.\n"); // not necessary, but classy

  pinMode(READ_PIN, INPUT);
}

void loop() {
  int lightLevel = analogRead(READ_PIN);

  Serial.println(lightLevel);

  delay(100);
}
