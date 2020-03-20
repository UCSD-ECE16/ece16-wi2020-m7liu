void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  setupButton();
  setupLED();
  setupMessage();
  setupMotor();
  setupADC();
  initDisplay();
  setupHR();
}

void loop() {
  Lab4();
  //receiveMessage();
}

void Lab1_C1(){
  condition6();
}

void Lab1(){
  if(getButton() == LOW){
    addTimer();
    delay(1000);
  }
  else{
    runTimer();
  }
}

void Lab2_C1(){
  buzzMotor(true);
  delay(1000);
  buzzMotor(false);
  delay(1000);
}

void Lab2_C2(){
  if (detectTap){
    addTimer();
  }
}

void Lab3(){
  stateMachineTimer();
}

void Lab4_Tutorial(){
  receiveMessage();
}


void Lab4(){
  receiveMessage();
  sendData();
}

void Lab5(){
  receiveMessage();
  sendData();
}
