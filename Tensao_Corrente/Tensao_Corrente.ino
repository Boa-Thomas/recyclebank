// Define analog voltage input
#define ANALOG_IN_PIN A0

// Define analog current input
#define CURRENT_PIN A1
 
// Floats for ADC voltage & Input voltage
float adc_voltage = 0.0;
float in_voltage = 0.0;
 
// Floats for resistor values in divider (in ohms)
float R1 = 30000.0;
float R2 = 7500.0; 
 
// Float for Reference Voltage
float ref_voltage = 5.0;
 
// Integer for ADC value
int adc_value = 0;
 
void setup(){
  // Setup Serial Monitor
  Serial.begin(9600);
}
 
void loop(){
  // Read the Analog Input
  adc_value = analogRead(ANALOG_IN_PIN);

  // Delay for voltage reading
  delay(2000);  // Delay for 2 seconds

  float AcsValue=0.0,Samples=0.0,AvgAcs=0.0,AcsValueF=0.0;
  
  for (int x = 0; x < 150; x++){ // Get 150 samples
    AcsValue = analogRead(CURRENT_PIN);     // Read current sensor values   
    Samples = Samples + AcsValue;  // Add samples together
    delay (5); // Let ADC settle before next sample (3ms)
  }

  AvgAcs = Samples / 150.0; // Taking Average of Samples

  AcsValueF = (2.45 - (AvgAcs * (5.0 / 1024.0)) )/0.100;

  Serial.print("Input Current = "); 
  Serial.println(AcsValueF, 3); // Print the read current on Serial monitor
  
  // Delay for current reading
  delay(3000);  // Delay for 3 seconds

  // Determine voltage at ADC input
  adc_voltage = (adc_value * ref_voltage) / 1024.0;
  
  // Calculate voltage at divider input
  in_voltage = adc_voltage * (R1 + R2) / R2;
  
  // Print results to Serial Monitor to 2 decimal places
  Serial.print("Input Voltage = ");
  Serial.println(in_voltage, 2);
  
  // Short delay
  delay(1000);  // Delay for 1 second
}