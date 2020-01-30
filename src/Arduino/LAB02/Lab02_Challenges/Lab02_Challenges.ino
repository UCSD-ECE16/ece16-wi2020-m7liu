//=======Global========//
int timer; //for millis() only
int delayed;
int tap_timer=0; //timer in seconds, go up when tapped, down when left for over 3 seconds

//=======OLDED========//
char message_buffer[4];

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  setupMotor();
  setupADC();
  initDisplay();
}

void loop() {
  // put your main code here, to run repeatedly:
  //Lab2_C1();
  //Lab2_C2();
  //receiveMessage();
  //Lab2_C4();
  stateMachineTimer();
}

void Lab2_C1(){
 // buzz motor at full power for 1 second

  buzzMotor(255);
  delay(1000);
 // buzz motor at half power for 1 second
  buzzMotor(127);
  delay(1000);
 // don’t buzz for 1 second
 buzzMotor(0);
 delay(1000);
}

void Lab2_C2(){
if(detectTap()) 
    //add one second to the timer and show on OLED
    addTimerOLED();
    
}

void Lab2_C4(){
  if (detectTap()){
    addTimerOLED();
    timer = millis();
    //update time of the last tap with millis()
  }
  //if time of last tap is more than 3 seconds ago
  if(millis()-timer>=3000){
    //run the timer
    runTimerOLED();
  }
}
