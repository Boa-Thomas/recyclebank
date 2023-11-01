void setup() {
  Serial.begin(9600); // Initialize serial communication at 9600 baud rate
}

void loop() {
  int sensorValue1 = analogRead(A0);  // Read sensor connected to A0
  int sensorValue2 = analogRead(A1);  // Read sensor connected to A1
  
  // Send the sensor data to Raspberry Pi
  Serial.print(sensorValue1);
  Serial.print(",");
  Serial.println(sensorValue2);
  
  delay(1000);  // Wait for 1 second
}
