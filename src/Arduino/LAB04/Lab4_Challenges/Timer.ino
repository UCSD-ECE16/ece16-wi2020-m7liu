// ========= Timer Var ========= //
int timer_seconds = 0;
int timer_state = 0; //States: 0 = Waiting for Tap, 1 = Adding Time to Timer, 2 = Count Down and Waiting for Disengage
long time_last_tap = 0;
long time_to_wait = 3000;

void addTimer(){
  timer_seconds++;
  printTime(timer_seconds);
}

void runTimer(){
  while(timer_seconds > 0){
    timer_seconds--;
    printTime(timer_seconds);
    delay(1000);
  }
}

void addTimerOLED(){
  timer_seconds++;
  String stringTime = String(timer_seconds);
  stringTime.toCharArray(in_text,4);
  showMessage(in_text, 1, true);
}

void runTimerOLED(){
  while(timer_seconds > 0){
    timer_seconds--;
    String stringTime = String(timer_seconds);
    stringTime.toCharArray(in_text,4);
    showMessage(in_text, 1, true);
    delay(1000);
  }
}



// ========== Timer Code ========= //
void stateMachineTimer(){
  if (timer_state == 0){ //Wait for first tap
    if (detectTap() == true){
      addTimerOLED();
      time_last_tap = millis();
      timer_state = 1;
    }
  }
  else if (timer_state == 1){//Add Time 
    if (detectTap() == true){
      addTimerOLED();
      time_last_tap = millis();
    }
    if (millis() - time_last_tap > time_to_wait){
      timer_state = 2;
    }
  }
  else if (timer_state == 2){ //Wait for Tap to disengage
    runTimerOLED();
    buzzMotor(255);
    if(detectTap()){
      buzzMotor(0);
      showMessage("Tap to Add Time", 1, true);
      timer_state = 0;
    }
  }
}
