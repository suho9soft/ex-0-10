#include <SPI.h>
#include <Ethernet2.h>

#define PWM_LED_PIN 6
#define LED1_PIN 7
#define LED2_PIN 8
#define LED3_PIN 9
#define LED4_PIN 10
#define LED5_PIN 11
#define LED6_PIN 12
#define LED7_PIN 13
#define LED8_PIN A0

// 네트워크 설정
byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };
IPAddress ip(172, 30, 1, 177);
EthernetServer server(8501);

int pwmBrightness = 0;
bool ledState[8] = {false, false, false, false, false, false, false, false};

void setup() {
  Serial.begin(9600);
  pinMode(PWM_LED_PIN, OUTPUT);
  analogWrite(PWM_LED_PIN, 0);

  pinMode(LED1_PIN, OUTPUT);
  pinMode(LED2_PIN, OUTPUT);
  pinMode(LED3_PIN, OUTPUT);
  pinMode(LED4_PIN, OUTPUT);
  pinMode(LED5_PIN, OUTPUT);
  pinMode(LED6_PIN, OUTPUT);
  pinMode(LED7_PIN, OUTPUT);
  pinMode(LED8_PIN, OUTPUT);

  Ethernet.begin(mac, ip);
  server.begin();
  Serial.print("Server is at ");
  Serial.println(Ethernet.localIP());
}

void loop() {
  EthernetClient client = server.available();
  if (client) {
    boolean currentLineIsBlank = true;
    String currentLine = "";
    bool brightnessUpdated = false;

    while (client.connected()) {
      if (client.available()) {
        char c = client.read();
        if (c == '\n' && currentLineIsBlank) {
          client.println("HTTP/1.1 200 OK");
          client.println("Content-Type: text/html");
          client.println("Connection: close");
          client.println();
          client.println("<!DOCTYPE HTML>");
          client.println("<html>");
          client.println("<head>");
          client.println("<title>Button and LED Control</title>");
          client.println("<style>");
          client.println("body { font-family: Arial, sans-serif; text-align: center; margin: 20px; background-color: #f0f0f0; }");
          client.println("h1 { color: #333; }");
          client.println("form { margin-top: 20px; display: inline-block; }");
          client.println("label, input { font-size: 16px; margin: 5px; }");
          client.println("input[type=number] { width: 80px; padding: 5px; }");
          client.println("input[type=submit] { padding: 10px 20px; background-color: #4CAF50; color: white; border: none; border-radius: 5px; cursor: pointer; font-family: 'Dancing Script', cursive; font-size: 20px; }");
          client.println("input[type=submit]:hover { background-color: #45a049; }");
          client.println(".feedback { margin-top: 20px; font-size: 18px; color: green; }");
          client.println("@import url('https://fonts.googleapis.com/css2?family=Dancing+Script&display=swap');");
          client.println("</style>");
          client.println("</head>");
          client.println("<body>");
          client.println("<h1>LED Control</h1>");
          client.print("<p>Current PWM LED brightness: <strong>");
          client.print(pwmBrightness);
          client.println("</strong></p>");

          // PWM 밝기 조절 폼
          client.println("<form action=\"\" method=\"GET\">");
          client.println("<label for=\"brightness\">Set PWM LED Brightness (0-255): </label>");
          client.println("<input type=\"number\" id=\"brightness\" name=\"brightness\" min=\"0\" max=\"255\" value=\"" + String(pwmBrightness) + "\">");
          client.println("<input type=\"submit\" value=\"Set Brightness\">");
          client.println("</form>");

          // 8개의 버튼 추가
          for (int i = 0; i < 8; i++) {
            client.println("<form action=\"\" method=\"GET\">");
            if (ledState[i]) {
              client.println("<input type=\"submit\" value=\"LED " + String(i+1) + " OFF\">");
            } else {
              client.println("<input type=\"submit\" value=\"LED " + String(i+1) + " ON\">");
            }
            client.println("<input type=\"hidden\" name=\"led\" value=\"" + String(i+1) + "\">");
            client.println("</form>");
          }

          client.println("<br><br>");
          client.println("</body>");
          client.println("</html>");
          break;
        }

        if (c == '\n') {
          currentLineIsBlank = true;
          if (currentLine.startsWith("GET /?brightness=")) {
            int start = currentLine.indexOf("=") + 1;
            int end = currentLine.indexOf(" ", start);
            int newBrightness = currentLine.substring(start, end).toInt();
            if (newBrightness >= 0 && newBrightness <= 255) {
              pwmBrightness = newBrightness;
              analogWrite(PWM_LED_PIN, pwmBrightness);
              brightnessUpdated = true;
            }
          }

          // LED 상태 변경
          if (currentLine.startsWith("GET /?led=")) {
            int start = currentLine.indexOf("=") + 1;
            int ledNumber = currentLine.substring(start).toInt();
            toggleLED(ledNumber);
          }

          currentLine = "";
        } else if (c != '\r') {
          currentLineIsBlank = false;
          currentLine += c;
        }
      }
    }
    delay(1);
    client.stop();
    Serial.println("Client disconnected!");
  }
}

void toggleLED(int ledNumber) {
  int pin;
  if (ledNumber >= 1 && ledNumber <= 8) {
    switch (ledNumber) {
      case 1: pin = LED1_PIN; break;
      case 2: pin = LED2_PIN; break;
      case 3: pin = LED3_PIN; break;
      case 4: pin = LED4_PIN; break;
      case 5: pin = LED5_PIN; break;
      case 6: pin = LED6_PIN; break;
      case 7: pin = LED7_PIN; break;
      case 8: pin = LED8_PIN; break;
      default: return;
    }
    // 토글된 상태에 맞게 LED 켜거나 끄기
    ledState[ledNumber - 1] = !ledState[ledNumber - 1]; // 상태 토글
    digitalWrite(pin, ledState[ledNumber - 1] ? HIGH : LOW);
  }
}
