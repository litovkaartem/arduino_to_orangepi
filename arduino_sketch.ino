int sen1, sen2, sen3, sen4, sen5;
char command; // Для хранения полученной команды

void setup() {
  // Начинаем последовательную связь на скорости 9600 бод
  Serial.begin(9600);
}

void loop() {
  // Проверка, есть ли доступные данные на серийном порту
  if (Serial.available() > 0) {
    command = Serial.read(); // Чтение команды от Orange Pi

    // Выполнение действия в зависимости от полученной команды
    switch (command) {
      case 'c': // Команда для сброса значений сенсоров
        sen1 = 0;
        sen2 = 0;
        sen3 = 0;
        sen4 = 0;
        sen5 = 0;
        break;
      // Добавьте дополнительные условия для других команд
      default:
        break;
    }
  }

  // Генерируем случайные значения для сенсоров
  sen1 = random(0, 100);
  sen2 = random(0, 100);
  sen3 = random(0, 100);
  sen4 = random(0, 100);
  sen5 = random(0, 100);

  // Формируем строку для передачи с разделителем
  String data = String(sen1) + "," + String(sen2) + "," + String(sen3) + "," + String(sen4) + "," + String(sen5);
  
  // Отправляем данные по последовательному порту
  Serial.println(data);

  // Ждем 1 секунду перед следующим обновлением
  delay(1000);
}
