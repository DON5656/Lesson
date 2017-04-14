int pin = 8;
unsigned long t0;
unsigned long ts = 30000; // 30000ms
unsigned long lowOc = 0;
float ratio = 0;
float concent = 0;

void setup() {
  Serial.begin(9600);
  pinMode(8,INPUT);
  t0 = millis();
}

void loop() {
  // LOWの占有率
  lowOc += pulseIn(pin, LOW);

  // サンプリング
  if ((millis() - t0) > ts){
    // LOWの割合
    ratio = lowOc/(ts*10.0);
    // ほこりの濃度を算出
    concent = 1.1 * pow(ratio,3) - 3.8 * pow(ratio,2) + 520 * ratio + 0.62;
    Serial.println(String(lowOc) + ","+String(ratio) + "," + String(concent));
    lowOc = 0;
    t0 = millis();
  }
}
