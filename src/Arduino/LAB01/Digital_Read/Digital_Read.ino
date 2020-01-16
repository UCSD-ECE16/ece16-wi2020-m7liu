int button_pin=25;

void setup() {
  // put your setup code here, to run once:
  pinMode(button_pin, INPUT_PULLUP);
  //pinMode(button_pin, INPUT);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (digitalRead(button_pin) == LOW) {
  digitalWrite(LED_BUILTIN, HIGH);
}
else {
  // Write your own code here to turn off the LED
  digitalWrite(LED_BUILTIN, LOW);
}

}
