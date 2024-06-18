// Define pins for RGB channels
const int redPin = 9;
const int greenPin = 10;
const int bluePin = 11;

void setup() {
  // Initialize serial communication
  Serial.begin(9600);

  // Set RGB pins as OUTPUT
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
}

void loop() {
  if (Serial.available()) {
    int volumeLevel = Serial.parseInt(); // Read volume level from serial

    // Map volume level (1-10) to brightness (0-255)
    int brightness = map(volumeLevel, 1, 10, 0, 255);

    // Set RGB channels to the same brightness
    analogWrite(redPin, brightness);
    analogWrite(greenPin, brightness);
    analogWrite(bluePin, brightness);
    
  }

  // Other loop code (if needed)
}