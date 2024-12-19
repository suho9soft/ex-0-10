#include <SPI.h>
#include <Ethernet2.h>

#define LED_PIN 6

// 네트워크 설정
byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };
IPAddress ip(172, 30, 1, 177);
EthernetServer server(8501);

int brightness = 0;

void setup() {
  Serial.begin(9600);
  pinMode(LED_PIN, OUTPUT);
  analogWrite(LED_PIN, 0);

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
          client.println("body { font-family: Arial, sans-serif; text-align: center; margin: 20px; }");
          client.println("h1 { color: #333; }");
          client.println("form { margin-top: 20px; }");
          client.println("label, input { font-size: 16px; }");
          client.println("input[type=number] { width: 80px; padding: 5px; margin-right: 10px; }");
          client.println("input[type=submit] { padding: 5px 15px; background-color: #007BFF; color: white; border: none; border-radius: 5px; cursor: pointer; }");
          client.println("input[type=submit]:hover { background-color: #0056b3; }");
          client.println(".feedback { margin-top: 20px; font-size: 18px; color: green; }");
          client.println("</style>");
          client.println("</head>");
          client.println("<body>");
          client.println("<h1>LED Control</h1>");
          client.print("<p>Current LED brightness: <strong>");
          client.print(brightness);
          client.println("</strong></p>");

          client.println("<form action=\"\" method=\"GET\">");
          client.println("<label for=\"brightness\">Set LED Brightness (0-255): </label>");
          client.println("<input type=\"number\" id=\"brightness\" name=\"brightness\" min=\"0\" max=\"255\" value=\"" + String(brightness) + "\">");
          client.println("<input type=\"submit\" value=\"Set Brightness\">");
          client.println("</form>");

          if (brightnessUpdated) {
            client.println("<p class=\"feedback\">Brightness updated successfully!</p>");
          }

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
              brightness = newBrightness;
              analogWrite(LED_PIN, brightness);
              brightnessUpdated = true;
            }
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
