int button_pin=26;
void setup() {
  // put your setup code here, to run once:
  pinMode(button_pin, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(button_pin, HIGH);
  delay(20);
  digitalWrite(button_pin, LOW);
  delay(1000);

}
