int StepperPins [] = {2,3,4,5};
int CurStep = 0;
int StepModes [4][4] = {
  {0, 2, 1, 3},
  {0, 3, 1, 2},
  {1, 3, 0, 2},
  {1, 2, 0, 3},
  };

void setup() {
  // put your setup code here, to run once:
  for (int pin : StepperPins) {
    pinMode(pin, OUTPUT);
    digitalWrite(pin, LOW);
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  Step(-1);
  delay(10);
}

void Step(int dir) {
  digitalWrite(StepperPins[StepModes[CurStep][2]], LOW);
  digitalWrite(StepperPins[StepModes[CurStep][3]], LOW);
  digitalWrite(StepperPins[StepModes[CurStep][0]], HIGH);
  digitalWrite(StepperPins[StepModes[CurStep][1]], HIGH);
  delay(10);
  digitalWrite(StepperPins[StepModes[CurStep][2]], LOW);
  digitalWrite(StepperPins[StepModes[CurStep][3]], LOW);
  digitalWrite(StepperPins[StepModes[CurStep][0]], LOW);
  digitalWrite(StepperPins[StepModes[CurStep][1]], LOW);
  CurStep += dir;
  if (CurStep > 3) {
    CurStep = 0;
  }
  if (CurStep < 0) {
    CurStep = 3;
  }
}

