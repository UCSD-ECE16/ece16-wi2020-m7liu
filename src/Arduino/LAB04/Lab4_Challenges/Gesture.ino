//Lab2_C3.ino
//TAP VARs
int threshZ = 2000;
int threshY = 1500;
int threshX = 0;

// ===== Gesture Code  ========//
bool detectTap(){
  readADC();
  bool tap_detected = false;
  if(accelZ_Val<threshZ & accelY_Val<threshY){
    tap_detected = true;
  }
  return tap_detected;
}
