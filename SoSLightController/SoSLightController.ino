#include <FastLED.h>

// How many leds in your strip?
#define NUM_LEDS 32


// For led chips like Neopixels, which have a data line, ground, and power, you just
// need to define DATA_PIN.  For led chipsets that are SPI based (four wires - data, clock,
// ground, and power), like the LPD8806, define both DATA_PIN and CLOCK_PIN
#define DATA_PIN 6

// Define the array of leds
CRGB leds[NUM_LEDS];

int incomingByte = 0; //incoming serial data

int fadeAmount = 5;  // Set the amount to fade I usually do 5, 10, 15, 20, 25 etc even up to 255.
int brightness = 0;

void setup() {
  Serial.begin(115200);
  Serial.println("resetting");
  FastLED.addLeds<NEOPIXEL, DATA_PIN>(leds, NUM_LEDS);
  LEDS.setBrightness(150);
}



void loop() {
  if (Serial.available() > 0) {
      // read the incoming byte:
      incomingByte = Serial.read();


      if (incomingByte == 48){ //if known record.
        startPlaying();
      } else if (incomingByte == 49){ // if stop
        stopPlaying();
      } else if (incomingByte == 50){ // if stop
        Circles();
      }else if (incomingByte == 51){ // if stop
        for (int i = 0; i <200; i++){
        idleState();
        }
      }
      }
  delay(100);
  }

void Circles() {
  for (int i = 1; i < NUM_LEDS/4; i++) {
  // Set the i'th led to red
  leds[i].setRGB( 0, 255, 0);
  leds[i+1].setRGB( 0, 50, 0);
  leds[i-1].setRGB( 0, 50, 0);
  leds[i+NUM_LEDS/2].setRGB(0,255,0);
  leds[i+NUM_LEDS/2+1].setRGB( 0, 50, 0);
  leds[i+NUM_LEDS/2-1].setRGB( 0, 50, 0);
  leds[i+NUM_LEDS/4].setRGB(0,255,0);
  leds[i+NUM_LEDS/4+1].setRGB( 0, 50, 0);
  leds[i+NUM_LEDS/4-1].setRGB( 0, 50, 0);
  leds[i+NUM_LEDS*3/4].setRGB(0,255,0);
  leds[i+NUM_LEDS*3/4+1].setRGB( 0, 50, 0);
  leds[i+NUM_LEDS*3/4-1].setRGB( 0, 50, 0);
 
  FastLED.show();
  // now that we've shown the leds, reset the i'th led to black
   leds[i] = CRGB::Black;
   leds[i-1]=CRGB::Black;
   leds[i+1]=CRGB::Black;
   leds[i+NUM_LEDS/2] = CRGB::Black;
   leds[i+NUM_LEDS/2 + 1] = CRGB::Black;
   leds[i+NUM_LEDS/2 - 1] = CRGB::Black;
   leds[i+NUM_LEDS/4] = CRGB::Black;
   leds[i+NUM_LEDS/4 - 1] = CRGB::Black;
   leds[i+NUM_LEDS/4 + 1] = CRGB::Black;
   leds[i+NUM_LEDS*3/4] = CRGB::Black;
   leds[i+NUM_LEDS*3/4 + 1] = CRGB::Black;
   leds[i+NUM_LEDS*3/4 - 1] = CRGB::Black;
  // Wait a little bit before we loop around and do it again
  delay(100);

  }
}

void startPlaying() {
  for (int i=0; i<5; i++){
    for (int j =0; j<NUM_LEDS; j++){
      leds[j].setRGB(0,230,0);
    }
    FastLED.show();
    delay(250);
    for (int j =0; j<NUM_LEDS; j++){
      leds[j].setRGB(0,0,0);
      
    }
    FastLED.show();
    delay(250);
  }
}


void stopPlaying() {
  for (int i=0; i<5; i++){
    for (int j =0; j<NUM_LEDS; j++){
      leds[j].setRGB(255,0,0);
    }
    FastLED.show();
    delay(250);
    for (int j =0; j<NUM_LEDS; j++){
      leds[j].setRGB(0,0,0);
      
    }
    FastLED.show();
    delay(250);
  }

}

void idleState(){
  for(int i = 0; i < NUM_LEDS; i++ )
   {
    leds[i].setRGB(200,50,5);  // Set Color HERE!!!
   leds[i].fadeLightBy(brightness);
  }
  FastLED.show();
  brightness = brightness + fadeAmount;
  // reverse the direction of the fading at the ends of the fade: 
  if(brightness == 0 || brightness == 255) {
    fadeAmount = -fadeAmount ; 
  }
  //Add Serial Read and check here?  If not idle, break  
  delay(20);  // This delay sets speed of the fade. I usually do from 5-75 but you can always go higher.
}

void clearLEDS(){
  for (int j =0; j<NUM_LEDS; j++){
      leds[j].setRGB(0,0,0);
      
    }
    FastLED.show();
  }
