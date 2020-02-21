int sampling_rate = 50; //sampling rate in Hz
unsigned long sampling_delay = calcSamplingDelay(sampling_rate); //microseconds between samples
unsigned long last_sample_time = 0; //microsecond of last sample
char in_text[64];                // Character buffer
int in_text_index = 0;
//int current_time = 0;

bool sending_data = false; //to send data?


void sendData(){
    if(sending_data){
      //current_time=micros();
        if(micros()-last_sample_time>=calcSamplingDelay(sampling_rate)){ //use non-blocking timing
            //update last_sample_time with current micros()
            last_sample_time = micros();  
            //read all ADC values
            readADC();
            //Serial print last_sample_time,x_val,y_val,z_val\n
            Serial.print(last_sample_time);
            //Serial.print("m");
            Serial.print(",");
            Serial.print(accelZ_Val);
            //Serial.print("n");
            Serial.print(",");
            Serial.print(accelY_Val);
            //Serial.print("o");
            Serial.print(",");
            Serial.print(accelX_Val);
            //Serial.print("p");
            Serial.print("\n");

            
        }
    }
}

long calcSamplingDelay(long sampling_rate){
    return (1000000.0/sampling_rate); //number of microseconds to wait between samples
}

void checkMessage(){
  String message = String(in_text); // converts in_text into a string
  // Check if message is “stop data” or “start data”.
  // set sending_data according to the message received 
  //delay for 1 second after setting sending_data to true.

  String start_data="start data";
  if(message=="start data"){
    sending_data=true;
    delay(2000);
  }
  if(message=="stop data"){
    sending_data=false;
  }
}


void receiveMessage(){
  if (Serial.available() > 0) { 
    char incomingChar = Serial.read();// read byte from serial
    if (incomingChar=='\n'){
      //show the in_text with show message
      showMessage(in_text, 1, true);
      //reset the in_text index back to 0
      checkMessage();
      in_text_index=0;
      memset(in_text,0,20); // this will clear the in_text buffer
    }
    else{
      //assign in_text[index] to the incoming char
      in_text[in_text_index]=incomingChar;
      //increment the index
      in_text_index++;
    }
  }
}
