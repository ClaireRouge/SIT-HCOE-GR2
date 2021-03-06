#define BRAKE 0
#define CW    1
#define CCW   2
#define CS_THRESHOLD 15   // Definition of safety current (Check: "1.3 Monster Shield Example").

    //MOTOR 1
#define MOTOR_A1_PIN 7
#define MOTOR_B1_PIN 8

    //MOTOR 2
#define MOTOR_A2_PIN 4
#define MOTOR_B2_PIN 9

#define PWM_MOTOR_1 5
#define PWM_MOTOR_2 6

#define CURRENT_SEN_1 A2
#define CURRENT_SEN_2 A3

#define EN_PIN_1 A0
#define EN_PIN_2 A1

#define MOTOR_1 0
#define MOTOR_2 1


class MotorControl {
    public:
    void setSpeed(int motor, int sped) {
      if (motor == 1) {
        if (sped < 0)
        {
          digitalWrite(MOTOR_A1_PIN, LOW);
          digitalWrite(MOTOR_B1_PIN, HIGH);
        }
        else if (sped > 0)
        {
          digitalWrite(MOTOR_A1_PIN, HIGH);
          digitalWrite(MOTOR_B1_PIN, LOW);
        }
        else
        {
          digitalWrite(MOTOR_A1_PIN, LOW);
          digitalWrite(MOTOR_B1_PIN, LOW);
        }

        analogWrite(PWM_MOTOR_1, abs(sped));
      }
      else if (motor == 2)
      {
        if (sped < 0)
        {
          digitalWrite(MOTOR_A2_PIN, LOW);
          digitalWrite(MOTOR_B2_PIN, HIGH);
        }
        else if (sped > 0)
        {
          digitalWrite(MOTOR_A2_PIN, HIGH);
          digitalWrite(MOTOR_B2_PIN, LOW);
        }
        else
        {
          digitalWrite(MOTOR_A2_PIN, LOW);
          digitalWrite(MOTOR_B2_PIN, LOW);
        }

        analogWrite(PWM_MOTOR_2, abs(sped));
      }
    }
};

MotorControl m;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  String s = Serial.readString();
  if (s != "") {
    m.setSpeed(1, s.substring(0,3).toInt());
    m.setSpeed(2, s.substring(3,6).toInt());
  }
}

