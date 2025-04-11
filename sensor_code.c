#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <RTClib.h>
#include <DHT.h>

#define DHTPIN 7    // Pin where the DHT11 is connected
#define DHTTYPE DHT11   // DHT 11

#define SENSOR_PIN A0  // Analog pin for both soil moisture and pH sensor
#define N_PIN A1  // Pin for N nutrient sensor
#define P_PIN A2  // Pin for P nutrient sensor
#define K_PIN A3  // Pin for K nutrient sensor

DHT dht(DHTPIN, DHTTYPE);

RTC_DS3231 rtc;

// Set the LCD address (usually 0x27 or 0x3F, check your display documentation)
const int I2C_ADDR = 0x27;
const int LCD_WIDTH = 16; // Adjust according to your LCD

// Define custom character for degree symbol
const uint8_t degreeSymbol[8] = {
  B00110,
  B01001,
  B01001,
  B00110,
  B00000,
  B00000,
  B00000,
  B00000
};

// Create an instance of the LiquidCrystal_I2C library
LiquidCrystal_I2C lcd(I2C_ADDR, LCD_WIDTH, 2);

enum DisplayState {
  DISPLAY_TEMPERATURE,
  DISPLAY_HUMIDITY,
  DISPLAY_WATER_LEVEL,
  DISPLAY_PH_VALUE,
  DISPLAY_NPK
};

DisplayState displayState = DISPLAY_TEMPERATURE;
unsigned long lastDisplayChangeTime = 0;

void setup() {
  // Initialize the LCD
  lcd.begin(LCD_WIDTH, 2);
  lcd.init();
  lcd.backlight();

  // Initialize the I2C communication
  Wire.begin();

  // Initialize the DHT sensor
  dht.begin();

  // Initialize the RTC
  if (!rtc.begin()) {
    lcd.print("RTC not found!");
    while (1);
  }

  // If the RTC lost power and isn't running, set the time
  if (rtc.lostPower()) {
    lcd.print("RTC lost power, setting time...");
    rtc.adjust(DateTime(F(_DATE), F(TIME_)));
  }

  // Create custom character for degree symbol
  lcd.createChar(1, degreeSymbol);

  // Initialize serial communication
  Serial.begin(9600);
}

void loop() {
  // Get the current time
  DateTime now = rtc.now();

  // Read temperature and humidity from DHT sensor
  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();

  // Read analog voltage from the sensor pin
  int sensorValue = analogRead(SENSOR_PIN);

  // Read analog voltage from NPK sensors
  int nLevel = map(analogRead(N_PIN), 0, 1023, 0, 100);
  int pLevel = map(analogRead(P_PIN), 0, 1023, 0, 100);
  int kLevel = map(analogRead(K_PIN), 0, 1023, 0, 100);

  // Interpret the sensor value differently based on the display state
  int waterLevel = map(sensorValue, 0, 1023, 100, 0); // Invert mapping for water level percentage
  int pHValue = map(sensorValue, 0, 1023, 14, 0); // Invert mapping for pH value (14-0)

  // Print sensor values to serial monitor
  Serial.print("Analog Sensor Value: ");
  Serial.println(sensorValue);
  Serial.print("Water Level: ");
  Serial.print(waterLevel);
  Serial.println("%");
  Serial.print("pH Value: ");
  Serial.println(pHValue);
  Serial.print("N Level: ");
  Serial.print(nLevel);
  Serial.println("%");
  Serial.print("P Level: ");
  Serial.print(pLevel);
  Serial.println("%");
  Serial.print("K Level: ");
  Serial.print(kLevel);
  Serial.println("%");

  // Display the time, date, and temperature on the LCD
  lcd.setCursor(0, 0);
  int hour_12 = now.hour() % 12;
  if (hour_12 == 0) {
    hour_12 = 12; // 12:00 AM
  }
  print2digits(hour_12);
  lcd.print(":");
  print2digits(now.minute());
  lcd.print(":");
  print2digits(now.second());
  lcd.print((now.hour() < 12) ? "AM" : "PM"); // Check for AM or PM
  lcd.print(" ");
  print2digits(now.day());
  lcd.print("/");
  print2digits(now.month());

  // Update display state every 5 seconds
  if (millis() - lastDisplayChangeTime >= 5000) {
    lastDisplayChangeTime = millis();
    switch (displayState) {
           case DISPLAY_TEMPERATURE:
        displayState = DISPLAY_HUMIDITY;
        break;
      case DISPLAY_HUMIDITY:
        displayState = DISPLAY_WATER_LEVEL;
        break;
      case DISPLAY_WATER_LEVEL:
        displayState = DISPLAY_PH_VALUE;
        break;
      case DISPLAY_PH_VALUE:
        displayState = DISPLAY_NPK;
        break;
      case DISPLAY_NPK:
        displayState = DISPLAY_TEMPERATURE;
        break;
    }
  }

  // Display sensor readings based on display state
  lcd.setCursor(0, 1); // Move cursor to the second line
  switch (displayState) {
    case DISPLAY_TEMPERATURE:
      lcd.print("Temp: ");
      lcd.print(temperature);
      lcd.write(1); // Display degree symbol
      lcd.print("C   ");
      break;
    case DISPLAY_HUMIDITY:
      lcd.print("Humidity: ");
      lcd.print(humidity);
      lcd.print("%   ");
      break;
    case DISPLAY_WATER_LEVEL:
      lcd.print("Water level: ");
      lcd.print(waterLevel);
      lcd.print("%   ");
      break;
    case DISPLAY_PH_VALUE:
      lcd.print("pH Value: ");
      lcd.print(pHValue);
      lcd.print("     ");
      break;
    case DISPLAY_NPK:
      lcd.print("N:");
      lcd.print(0);
      lcd.print("% P:");
      lcd.print(0);
      lcd.print("% K:");
      lcd.print(0);
      lcd.print("%  ");
      break;
  }

  delay(1000); // Update every second
}

void print2digits(int number) {
  if (number < 10) {
    lcd.print("0");
  }
  lcd.print(number);
}
