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

#include <Wire.h>
#include <LIDARLite.h>
#include <Servo.h>
// Globals
LIDARLite lidarLite;
Servo myservo;

int cal_cnt = 0;
int data[50][2];
int curData = 0;
int pos = 0; //servo pos


void setup()
{
  Serial.begin(115200); // Initialize serial connection to display distance readings

  lidarLite.begin(0, true); // Set configuration to default and I2C to 400 kHz
  lidarLite.configure(0); // Change this number to try out alternate configurations
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
  myservo.write(90);
}

void distance(){
  int dist;
  // At the beginning of every 100 readings,
  // take a measurement with receiver bias correction
  if ( cal_cnt == 0 ) {
    dist = lidarLite.distance();      // With bias correction
  } else {
    dist = lidarLite.distance(false); // Without bias correction
  }

  // Increment reading counter
  cal_cnt++;
  cal_cnt = cal_cnt % 100;
  
  data[curData][0] = dist;
  data[curData][1] = pos;
  curData++;
}

void sendData(){
  Serial.write(sizeof(int)*(curData)*2);
  Serial.write((uint8_t*)data,sizeof(int)*(curData)*2);
  curData = 0;
}

void loop()
{
  for (pos = 45; pos <= 135; pos += 5) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    distance();
    delay(13);                       // waits 15ms for the servo to reach the position
  }
  for (pos = 135; pos >= 45; pos -= 5) { // goes from 180 degrees to 0 degrees
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    distance();
    delay(13);                       // waits 15ms for the servo to reach the position
  }
  sendData();
}
