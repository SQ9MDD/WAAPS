#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>

#define SEALEVELPRESSURE_HPA (1013.25)

Adafruit_BME280 bme;

void setup() {
  Serial.begin(9600);

  if (!bme.begin(0x76)) {
    Serial.println("Could not find a valid BME280 sensor, check wiring!");
    while (1);
  }
  delay(1000);
  Serial.print("WAAPS300");
  Serial.print("*");
  Serial.print(bme.readTemperature());
  Serial.print("*");
  Serial.print(bme.readPressure() / 100.0F);
  Serial.print("*");
  Serial.print(bme.readHumidity());
}

void loop() {
  delay(1000);
}
