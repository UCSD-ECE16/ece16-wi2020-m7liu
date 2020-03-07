int button_pin = 25;

void setupButton(){
  pinMode(button_pin, INPUT);
}

bool getButton(){
  bool button_val = digitalRead(button_pin);
  return button_val;
}
