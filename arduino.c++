const int redLED = 9;
const int greenLED = 10;
const int blueLED = 11;
const int whiteLED = 12;

void setup() {
    Serial.begin(9600);
    pinMode(redLED, OUTPUT);
    pinMode(greenLED, OUTPUT);
    pinMode(blueLED, OUTPUT);
    pinMode(whiteLED, OUTPUT);
}

void loop() {
    if (Serial.available() > 0) {
        String colorName = Serial.readStringUntil('\n');
        colorName.trim();

        // Apagar todos los LEDs antes de encender el correcto
        digitalWrite(redLED, LOW);
        digitalWrite(greenLED, LOW);
        digitalWrite(blueLED, LOW);
        digitalWrite(whiteLED, LOW);

        // Encender el LED correspondiente
        if (colorName == "Red") {
            digitalWrite(redLED, HIGH);
        } else if (colorName == "Green") {
            digitalWrite(greenLED, HIGH);
        } else if (colorName == "Blue") {
            digitalWrite(blueLED, HIGH);
        } else if (colorName == "White") {
            digitalWrite(whiteLED, HIGH);
        }
    }
}
