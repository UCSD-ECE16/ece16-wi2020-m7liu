//ACCEL VARs
int accelZ = A0;
int accelY = 39;//assign pin value
int accelX = 34;//assign pin value
int accelZ_Val = 0;//set to 0
int accelY_Val = 0;//set to 0
int accelX_Val = 0;//set to 0

// ======== ADC Code ======== //
void setupADC(){
  //setup each accel pins to be an input pin
  pinMode(accelZ, INPUT);
  pinMode(accelY, INPUT);
  pinMode(accelX, INPUT);
}

void readADC(){
  //read each accel pin and assign value to the corresponding Val
  accelZ_Val=analogRead(accelZ);
  accelY_Val=analogRead(accelY);
  accelX_Val=analogRead(accelX);
}

void printADC(){ //print the ADC values
  Serial.print("Z:");
  Serial.print(accelZ_Val);
  Serial.print(",");
  Serial.print("Y:");
  Serial.print(accelY_Val);
  Serial.print(",");
  Serial.print("X:");
  Serial.println(accelX_Val);
}
