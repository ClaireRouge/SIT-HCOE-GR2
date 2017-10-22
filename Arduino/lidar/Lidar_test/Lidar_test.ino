/**
 * LIDARLite I2C Example
 * Author: Garmin
 * Modified by: Shawn Hymel (SparkFun Electronics)
 * Date: June 29, 2017
 * 
 * Read distance from LIDAR-Lite v3 over I2C
 * 
 * See the Operation Manual for wiring diagrams and more information:
 * http://static.garmin.com/pumac/LIDAR_Lite_v3_Operation_Manual_and_Technical_Specifications.pdf
 */

//#include <Wire.h>
//#include <LIDARLite.h>
//#include <Servo.h>
// Globals
//LIDARLite lidarLite;
//Servo myservo;

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

int cal_cnt = 0;
int data[50][2]; //rember to increase this size with the amount of sensors readings
int curData = 0;
int pos = 0; //servo pos

int testdata[3][8][2] = {
  {{3,0},{6,1},{0,2},{6,3},{7,3},{3,2},{2,1},{2,0}},
  {{664,0},{894,1},{673,2},{853,3},{23,3},{212,2},{856,1},{853,0}},
  {{0,0},{0,0},{0,0},{0,0},{0,0},{0,0},{0,0},{0,0}}
};
int testnr = 0; 
int m1 = 0;
int m2 = 0;

void setup()
{
  Serial.begin(115200); // Initialize serial connection to display distance readings

  //lidarLite.begin(0, true); // Set configuration to default and I2C to 400 kHz
  //lidarLite.configure(0); // Change this number to try out alternate configurations
  //myservo.attach(9);  // attaches the servo on pin 9 to the servo object
  //myservo.write(45);
  pinMode(LED_BUILTIN, OUTPUT); // for testing
}

void distance(){
  int dist = 0;
  // At the beginning of every 100 readings,
  // take a measurement with receiver bias correction
  if ( cal_cnt == 0 ) {
    //dist = lidarLite.distance();      // With bias correction
  } else {
    //dist = lidarLite.distance(false); // Without bias correction
  }

  // Increment reading counter
  cal_cnt++;
  cal_cnt = cal_cnt % 100;
  
  data[curData][0] = dist;
  data[curData][1] = pos;
  curData++;
}

void sendData(){
  /*
  Serial.write(sizeof(int)*(curData)*2);
  Serial.write((uint8_t*)data,sizeof(int)*(curData)*2);
  */
  Serial.write(sizeof(int)*7*2);
  Serial.write((uint8_t*)testdata[m1],sizeof(int)*7*2);
  curData = 0;
}

void my_delay(int delaytime){
  //Serial.println("a")
  unsigned long starttime = millis();
  //Serial.println("b")
  if (Serial.available() > 1) {
    //Serial.println("c")
    //m.setSpeed(1, (int(Serial.read())-128)*2);
    //m.setSpeed(2, (int(Serial.read())-128)*2);
    int m1 = (int(Serial.read())-128)*2;
    //Serial.println("d")
    int m2 = (int(Serial.read())-128)*2;
    //Serial.println("e")
    sendData();
    //Serial.println("f")
  }
  unsigned long endtime = millis();
  if(endtime -starttime < delaytime){
    delay(delaytime - (endtime -starttime));
  } else{
    digitalWrite(LED_BUILTIN, HIGH);
  }
}

void loop(){
  for (pos = 20; pos <= 160; pos += 4) { // goes from 0 degrees to 180 degrees. Its important not to hit 90
    //Serial.print(pos);
    // in steps of 1 degree
    //myservo.write(pos);              // tell servo to go to position in variable 'pos'
    distance();
    my_delay(12);                       // waits 15ms for the servo to reach the position
  }
  for (pos = 160; pos >= 20; pos -= 4) { // goes from 180 degrees to 0 degrees
    //myservo.write(pos);              // tell servo to go to position in variable 'pos'
    //Serial.print(pos);
    distance();
    my_delay(12);                       // waits 15ms for the servo to reach the position
  }
  
}
