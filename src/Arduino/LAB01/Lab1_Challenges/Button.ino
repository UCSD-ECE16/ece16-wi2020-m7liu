int button_pin = 25;

void setupButton(){
  // setup pin mode
  pinMode(button_pin, INPUT);
}

bool getButton(){
  bool button_val = digitalRead(button_pin); //read value of button pin
  return button_val;
}
