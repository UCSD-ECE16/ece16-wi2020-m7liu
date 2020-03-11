//Lab2_Tutorial_Accel.ino
//ACCEL VARs
int accelZ = A0;
int accelY = 39;
int accelX = 34;
int accelZ_Val = 0;
int accelY_Val = 0;
int accelX_Val = 0;

// ======== ADC Code ======== //
void setupADC(){
  pinMode(accelZ, INPUT);
  pinMode(accelY, INPUT);
  pinMode(accelX, INPUT);
}

void readADC(){
  accelZ_Val = analogRead(accelZ);
  accelY_Val = analogRead(accelY);
  accelX_Val = analogRead(accelX); 
}

void printADC(){
  Serial.print("Z:");
  Serial.print(accelZ_Val);
  Serial.print(",");
  Serial.print("Y:");
  Serial.print(accelY_Val);
  Serial.print(",");
  Serial.print("X:");
  Serial.println(accelX_Val);
}
