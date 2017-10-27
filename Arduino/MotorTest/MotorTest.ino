int Q1 = 5;
int Q2 = 6;

void setup() {
  // put your setup code here, to run once:
  pinMode(Q1, OUTPUT);
  pinMode(Q2, OUTPUT);
  analogWrite(Q1,0);
  analogWrite(Q2,255);
}

void loop() {
  // put your main code here, to run repeatedly:
}

