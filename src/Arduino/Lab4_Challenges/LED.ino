// Lab1_C1
int red_led = 26;
int yellow_led = 27;
int blue_led = 13;

void setupLED(){
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(red_led, OUTPUT);
  pinMode(yellow_led, OUTPUT);
  pinMode(blue_led, OUTPUT);
}

void condition1(){
  digitalWrite(LED_BUILTIN, LOW);
  delay(500);
  digitalWrite(LED_BUILTIN, HIGH);
  delay(500);
}

void condition2(){
  digitalWrite(LED_BUILTIN, LOW);
  delay(50);
  digitalWrite(LED_BUILTIN, HIGH);
  delay(50);
}

void condition3(){
  digitalWrite(LED_BUILTIN, LOW);
  delay(10);
  digitalWrite(LED_BUILTIN, HIGH);
  delay(10);
}

void condition4(){
  digitalWrite(red_led, LOW);
  delay(1000);
  digitalWrite(red_led, HIGH);
  delay(100);
}

void condition5(){
  digitalWrite(yellow_led, LOW);
  delay(200);
  digitalWrite(yellow_led, HIGH);
  delay(50);
}

void condition6(){
  digitalWrite(blue_led, LOW);
  delay(20);
  digitalWrite(blue_led, HIGH);
  delay(10);
}
