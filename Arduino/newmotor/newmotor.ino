//MOTOR 0
#define MOTOR_0_DIG_FOR 23
#define MOTOR_0_DIG_BACK 25

#define MOTOR_0_PWM_FOR 10
#define MOTOR_0_PWM_BACK 9

//MOTOR 1
#define MOTOR_1_DIG_FOR 27
#define MOTOR_1_DIG_BACK 29

#define MOTOR_1_PWM_FOR 12
#define MOTOR_1_PWM_BACK 11

// motor_num, Forward/backwards, dig(0)/pwm
int motorPin[2][2][2]{
  {
    {MOTOR_0_DIG_FOR,MOTOR_0_PWM_FOR},{MOTOR_0_DIG_BACK,MOTOR_0_PWM_BACK}
  },
  {
    {MOTOR_1_DIG_FOR,MOTOR_1_PWM_FOR},{MOTOR_1_DIG_BACK,MOTOR_1_PWM_BACK}
  }
};


class MotorControl{
  public:
  void setSpeed(int motor,int motorSpeed){
    int* onPins = motorPin[motor][motorSpeed < 0]; //should get an array with the correct dig and pwm pin
    int* offPins = motorPin[motor][motorSpeed > 0];
    //Serial.println(motorSpeed);
    digitalWrite(offPins[0],LOW);
    analogWrite(offPins[1],0);
    //Serial.println(offPins[0]);
    //Serial.println(offPins[1]);
    
    digitalWrite(onPins[0],HIGH);
    analogWrite(onPins[1],motorSpeed);
    //Serial.println(onPins[0]);
    //Serial.println(onPins[1]);
    //Serial.println("done");
  }
};

MotorControl m;

void setup() {
  // put your setup code here, to run once:
  for(int i = 0;i < 2;i++){
    for(int j = 0;j < 2;j++){
      for(int k = 0;k < 2;k++){
        pinMode(motorPin[i][j][k],OUTPUT);
      }
    }
  }
  m.setSpeed(0, 0);
  m.setSpeed(1, 0);
  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 1){
    m.setSpeed(0, (int(Serial.read())-128)*2);
    m.setSpeed(1, (int(Serial.read())-128)*2); 
    Serial.println("K");
    Serial.flush();
  }
}
