int timer;
void setup() {
  // put your setup code here, to run once:
  setupLED();
  setupButton();
  setupMessage();
}

void Lab1_C2(){
  if(getButton()==LOW){ //button value is pressed
      //add one second to the timer
      Serial.println("TIMER:");
      timer = millis();
      Serial.println(timer);
      addTimer();
      //wait one second
      delay(1000);
  }
  else{
    runTimer();
  }

}
void loop() {
  // put your main code here, to run repeatedly:
  //condition1();
  //condition2();
  //condition3();
  //condition4();
  //condition5();
  //condition6();
  //Challenge 2
  Lab1_C2();

}
