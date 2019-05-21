#if 0
#include <SPI.h>
#include <PN532_SPI.h>
#include <PN532.h>
#include <NfcAdapter.h>

PN532_SPI pn532spi(SPI, 10);
NfcAdapter nfc = NfcAdapter(pn532spi);
#else

#include <Wire.h>
#include <PN532_I2C.h>
#include <PN532.h>
#include <NfcAdapter.h>

PN532_I2C pn532_i2c(Wire);
NfcAdapter nfc = NfcAdapter(pn532_i2c);
#endif
void writeString(String stringData) { // Used to serially push out a String with Serial.write()

  for (int i = 0; i < stringData.length(); i++)
  {
    Serial.write(stringData[i]);   // Push each char 1 by 1 on each loop pass
  }

}// end writeString

//def checkTag
void setup(void) {
  Serial.begin(115200);
  Serial.println("NDEF Reader");
  nfc.begin();
}

void loop(void) {
  if (nfc.tagPresent())
  {
    NfcTag tag = nfc.read();
    Serial.println(tag.getUidString());
  
  }
  else {
    Serial.println("n");
  }
  delay(50);
}
