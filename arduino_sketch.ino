// ���������� ���������� ��� ��������
int sen1, sen2, sen3, sen4, sen5;

void setup() {
  // �������� ���������������� ����� �� �������� 9600 ���
  Serial.begin(9600);
}

void loop() {
  // ���������� ��������� �������� ��� ��������
  sen1 = random(0, 100);
  sen2 = random(0, 100);
  sen3 = random(0, 100);
  sen4 = random(0, 100);
  sen5 = random(0, 100);

  // ��������� ������ ��� �������� � ������������
  String data = String(sen1) + "," + String(sen2) + "," + String(sen3) + "," + String(sen4) + "," + String(sen5);
  
  // ���������� ������ �� ����������������� �����
  Serial.println(data);

  // ���� 1 ������� ����� ��������� �����������
  delay(1000);
}