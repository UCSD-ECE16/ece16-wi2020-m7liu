//Lab2_C1.ino
// setting PWM properties
const int pwmFrequency = 5000;
const int pwmChannel = 3;
const int pwmBitResolution = 8;

//MOTOR VARs
bool increasing = true;
int motorPin = 5;
int pwm_output = 0;

// ========== Motor Code =========//

void setupMotor(){
    // configure PWM functionalities
  ledcSetup(pwmChannel, pwmFrequency, pwmBitResolution);
    
  // attach the pwmChannel to the outputGPIO to be controlled
  ledcAttachPin(motorPin, pwmChannel);
}

void buzzMotor(int buzz_power){
  ledcWrite(pwmChannel, buzz_power);
}
