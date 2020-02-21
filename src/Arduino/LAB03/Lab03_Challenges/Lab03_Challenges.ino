//=======Global========//
int timer; //for millis() only
int delayed;
int tap_timer=0; //timer in seconds, go up when tapped, down when left for over 3 seconds

//=======OLDED========//
char message_buffer[4];

void setup(){
  Serial.begin(115200);
  initDisplay();
  setupMotor();
  setupADC();
  
}
void loop(){
  //sendData();
  //receiveMessage();
    Lab3();
}

void Lab3(){
    receiveMessage(); //checks for serial message
    sendData(); //sends data via serial if suppose to
}
