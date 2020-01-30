// ========= Timer Var ========= //
unsigned long time_last_tap = 0; //initiate the last tap time at 0
int timer_state=0;
int motorBlock;
// ========== Timer Code ========= //
void runTimerOLED(){
  while(tap_timer > 0){
    tap_timer--;
    // print to OLED instead of Serial.
     String stringTime = String(tap_timer);//convert timer_seconds to string
     stringTime.toCharArray(message_buffer,4); //convert string to char buffer
     // show message_buffer with showMessage
     showMessage(message_buffer, 1, true);
     delay(1000);
  }
}

void stateMachineTimer(){
  if (timer_state == 0){
      if (detectTap()){
         addTimerOLED();
         timer = millis();
      }
      /*if(tap_timer==0){
        timer_state=0;
      }*/
      else{
        timer_state = 1; //proceed to 1
      }
      motorBlock=0;
  }
  else if (timer_state == 1){
    if(millis()-timer>=3000){
       //run the timer
       timer_state = 2; //proceed to 2
     }
     else{
        timer_state = 0; // go back to 0
     }
     
  }
  else if (timer_state == 2){
    runTimerOLED(); //decrement until 0
    timer_state = 4; //proceed to 4
  }
  else if (timer_state == 4){
    buzzMotor(255);
    if(detectTap()){
      buzzMotor(0);
      timer_state = 0; //proceed to 0

      //delay(30); //wait a bit so the taps do not overlap
    }

  }
}
