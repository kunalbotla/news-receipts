/*
 * created by Rui Santos, https://randomnerdtutorials.com
 * 
 * Complete Guide for Ultrasonic Sensor HC-SR04
 *
    Ultrasonic sensor Pins:
        VCC: +5VDC
        Trig : Trigger (INPUT) - Pin11
        Echo: Echo (OUTPUT) - Pin 12
        GND: GND
 */
 
int trigPin = 11;    // Trigger
int echoPin = 12;    // Echo
long duration, cm, inches;

#include <Servo.h>
Servo servo;
int servoPin = 9;    // servo
int pos = 0;
 
void setup() {
  //Serial Port begin
  Serial.begin (9600);
  //Define inputs and outputs
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  
  servo.attach(servoPin);  // attaches the servo on pin 9 to the servo object	10	
}
 
void loop() {
  // The sensor is triggered by a HIGH pulse of 10 or more microseconds.
  // Give a short LOW pulse beforehand to ensure a clean HIGH pulse:
  digitalWrite(trigPin, LOW);
  delayMicroseconds(5);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
 
  // Read the signal from the sensor: a HIGH pulse whose
  // duration is the time (in microseconds) from the sending
  // of the ping to the reception of its echo off of an object.
  pinMode(echoPin, INPUT);
  duration = pulseIn(echoPin, HIGH);
 
  // Convert the time into a distance
  cm = (duration/2) / 29.1;     // Divide by 29.1 or multiply by 0.0343
  inches = (duration/2) / 74;   // Divide by 74 or multiply by 0.0135
  
  Serial.print(inches);
  Serial.print("in, ");
  Serial.print(cm);
  Serial.print("cm");
  Serial.println();
  
  delay(250);
  
  if (inches > 3) {
   
    servo.write(180);
  
  //   for (pos = 70; pos <= 180; pos += 1) { // goes from 0 degrees to 180 degrees	14	    
  // // in steps of 1 degree	15	    
  // servo.write(pos);             // tell servo to go to position in variable 'pos'	16	    
  // delay(15);
  // }
  }
  else {
    delay(20);
  }
  
  // for (pos = 70; pos <= 180; pos += 1) { // goes from 0 degrees to 180 degrees	14	    
  // // in steps of 1 degree	15	    
  // servo.write(pos);              // tell servo to go to position in variable 'pos'	16	    
  // delay(15);                       // waits 15ms for the servo to reach the position	17	  
  // }	// 18	  
  // for (pos = 180; pos >= 70; pos -= 1) { // goes from 180 degrees to 0 degrees	19
  // servo.write(pos);              // tell servo to go to position in variable 'pos'	20
  // delay(15);                       // waits 15ms for the servo to reach the position	21
  // }
}
