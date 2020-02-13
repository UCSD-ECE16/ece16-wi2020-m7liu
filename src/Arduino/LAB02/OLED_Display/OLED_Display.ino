void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  initDisplay();
  //showMessage("Initializing...", 1, true);
  //showMessage("Success!", 2, false);


}

void loop() {
  // put your main code here, to run repeatedly:
  receiveMessage();

}
