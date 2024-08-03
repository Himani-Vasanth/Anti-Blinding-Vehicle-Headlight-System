#include <Adafruit_NeoPixel.h>

#define PIN        6  // Pin for LED Matrix
#define NUM_LEDS  64  // Number of LEDs in your matrix

Adafruit_NeoPixel matrix = Adafruit_NeoPixel(NUM_LEDS, PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  Serial.begin(9600);
  matrix.begin();
  matrix.show();  // Initialize all pixels to 'off'
}

void loop() {
  if (Serial.available() > 0) {
    char lane = Serial.read();  // Read the lane information from Python

    // Control LEDs based on the received lane information
    for (int i = 0; i < NUM_LEDS; i++) {
      int row = i / 8;  // Calculate row index
      int col = i % 8;  // Calculate column index

      // Determine which LEDs to turn on based on the lane
      if ((lane == 'l' && col < 4) || (lane == 'r' && col >= 4)) {
        matrix.setPixelColor(i, matrix.Color(255, 255, 255));  // White color for LEDs in the lane
      } else {
        matrix.setPixelColor(i, matrix.Color(0, 0, 0));  // Turn off other LEDs
      }
    }

    matrix.show();  // Update the LED matrix
  }
}