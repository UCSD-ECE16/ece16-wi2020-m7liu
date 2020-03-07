/*
//OLED VARs
char in_text[20];                // Character buffer
int in_text_index = 0;

bool send_data = false; //initialize with data sending as false

long last_send = 0;

long sampling_rate = 100;
long sampling_delay = calcSamplingDelay(sampling_rate); 

#include "BluetoothSerial.h"
BluetoothSerial SerialBT;

void setupMessage(){
  SerialBT.begin("Edward_FireBeetle"); //defaults to 115200
}

void printTime(int seconds){
  SerialBT.println(seconds);
}

long calcSamplingDelay(long sampling_rate){
  return 1000000/sampling_rate;
}

void sendData(){
  if(micros()-last_send > sampling_delay & send_data){
    last_send = micros();
    readADC();
    readHR();
    SerialBT.print(micros());
    SerialBT.print(',');
    SerialBT.print(accelX_Val);
    SerialBT.print(',');
    SerialBT.print(accelY_Val);
    SerialBT.print(',');
    SerialBT.print(accelZ_Val);
    SerialBT.print(',');
    SerialBT.print(HR_Red);
    SerialBT.print(',');
    SerialBT.print(HR_IR);
    SerialBT.print(',');
    SerialBT.println(HR_Green);
  }
}

void receiveMessage(){
  if (SerialBT.available() > 0) {
    char incomingChar = SerialBT.read();
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
  if(message == "Stop Data"){
    send_data = false;
  }
  else if(message=="Start Data"){
    send_data = true;
    delay(1);
  }
}
*/
