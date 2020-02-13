//TAP VARs
int normZ=2280;
int normY=1730;
int normX=1790;
int threshZ = 150;//determine the threshold you need
int threshY = 0;
int threshX = 0;
int timeHigh=30;
int tapTime=0;

// ===== Gesture Code  ========//
bool detectTap(){
  //read the ADC values. Note that the ADC values are global so you don’t need to define a local variable for them.
  readADC();
   
  bool tap_detected = false; // first set to false
  /*if((accelZ_Val-normZ>threshZ || normZ-accelZ_Val>threshZ)&&tapTime>=timeHigh){
    tap_detected = true; //if the accel values meet the rule, set to true
    Serial.println("Detected");
  }*/
  if(accelZ_Val-normZ>threshZ || normZ-accelZ_Val>threshZ){
  tap_detected=true;
  }
/*  if(tapTime>timeHigh){
    tapTime=0;
    
  }*/
  return tap_detected;
}
