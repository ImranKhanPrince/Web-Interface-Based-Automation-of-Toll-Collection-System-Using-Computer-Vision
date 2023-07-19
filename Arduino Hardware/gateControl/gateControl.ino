#include <Servo.h>

const int triggerPin = 6;  // Sonar sensor trigger pin
const int echoPin = 5;     // Sonar sensor echo pin
const int servoPin = 9;    // Servo motor signal pin

const int thresholdDistance = 17;  // Threshold distance in centimeters
    int i;
    int j;
Servo myservo;

void setup() {
  pinMode(triggerPin, OUTPUT);
  pinMode(echoPin, INPUT);

  myservo.attach(servoPin);

  Serial.begin(9600);  // Initialize serial communication
}

void loop() {
  long duration, distance;

  // Generate a short pulse to the sonar sensor to start measurement
  digitalWrite(triggerPin, LOW);
  delayMicroseconds(2);
  digitalWrite(triggerPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(triggerPin, LOW);

  // Measure the duration of the pulse from the sonar sensor
  duration = pulseIn(echoPin, HIGH);

  // Calculate the distance based on the speed of sound
  distance = duration / 58.2;  // Divide by 58.2 to convert microseconds to centimeters

  // Check the distance and control the servo motor accordingly
  if ((distance <= thresholdDistance && Serial.available() > 0) && (Serial.available() > 0 && Serial.readStringUntil('\n') == "Verified")) 
  {
    myservo.write(90);  // Rotate the servo to 90 degrees
    
    // Serial.println("Servo rotated to 90 degrees.");
  } 
  else if (distance > thresholdDistance || (Serial.available() > 0 && Serial.readStringUntil('\n') == "notVerified")) 
  {
    delay(1000);
    myservo.write(0);  // Rotate the servo to 0 degrees
    
    // Serial.println("Servo rotated to 0 degrees.");
  }

  delay(100);  // Delay between measurements (adjust as needed)
}
