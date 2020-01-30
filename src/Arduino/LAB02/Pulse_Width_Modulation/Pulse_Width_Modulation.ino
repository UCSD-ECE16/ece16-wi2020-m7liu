#include <Wire.h>

// setting PWM properties
const int pwmFrequency = 5000;
const int pwmChannel = 0;
const int pwmBitResolution = 8;
void setup() {
  // put yoWur setup code here, to run once:
  // configure PWM functionalities
  ledcSetup(pwmChannel, pwmFrequency, pwmBitResolution);
  
  // attach the pwmChannel to the outputGPIO to be controlled
  ledcAttachPin(LED_BUILTIN, pwmChannel);
}

void loop() {
  // put your main code here, to run repeatedly:
  delay(100);
  //ledcWrite will write the value to the pwmChannel
  ledcWrite(pwmChannel, 0);
  delay(100);
  ledcWrite(pwmChannel, 127);
  delay(100);
  ledcWrite(pwmChannel, 255);
  delay(100);
  ledcWrite(pwmChannel, 127);

}
