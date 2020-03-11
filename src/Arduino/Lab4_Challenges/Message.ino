
//OLED VARs
char in_text[20];                // Character buffer
int in_text_index = 0;

bool send_data = false; //initialize with data sending as false

unsigned long last_send = 0;

unsigned long sampling_rate = 50;
unsigned long sampling_delay = calcSamplingDelay(sampling_rate); 


void setupMessage(){
  Serial.begin(115200);
}

void printTime(int seconds){
  Serial.println(seconds);
}

long calcSamplingDelay(long sampling_rate){
  return 1000000/sampling_rate;
}

void sendData(){
  if(micros()-last_send > sampling_delay & send_data){
    last_send = micros();
    readADC();
    readHR();
    Serial.print(last_send);
    Serial.print(',');
    Serial.print(accelX_Val);
    Serial.print(',');
    Serial.print(accelY_Val);
    Serial.print(',');
    Serial.print(accelZ_Val);
    Serial.print(',');
    Serial.println(HR_Data);
  }
}

void receiveMessage(){
  if (Serial.available() > 0) {
    char incomingChar = Serial.read();
    if (incomingChar == '\n'){
      showMessage(in_text,1,true);
      checkMessage();
      in_text_index = 0;
      memset(in_text,0,20);
    }
    else{
      in_text[in_text_index] = incomingChar;
      in_text_index++;
    }
  }
}

void checkMessage(){
  String message = String(in_text);
  if(message == "stop data"){
    send_data = false;
  }
  else if(message=="start data"){
    send_data = true;
    delay(1000);
  }
}
