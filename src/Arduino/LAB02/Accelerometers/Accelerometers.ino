int accelz=A0;
int timer;
int delayed=20;
void setup() {
  // put your setup code here, to run once:
  pinMode(accelz,INPUT);
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  int accelz_val=analogRead(accelz);
  Serial.println(accelz_val);
  Serial.print(0);
  Serial.print(" ");
  Serial.print(4000);
  Serial.print(" ");
  //Serial.println((accelz_val/4096)*3.3);
  timer=millis();
  while(millis()<delayed+timer){
  }
}
