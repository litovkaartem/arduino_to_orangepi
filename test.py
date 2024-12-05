import serial
import time

def main():
    # Устанавливаем соединение через последовательный порт
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)  # Укажите правильный порт
    time.sleep(2)  # Ждем инициализации порта

    while True:
        try:
            # Чтение данных от Arduino
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').strip()  # Читаем строку и очищаем от лишних символов
                print(f"Получено от Arduino: {line}")

                # Разделяем полученную строку на значения
                data = line.split(",")
                if len(data) == 5:  # Проверяем, что строка содержит 5 переменных
                    try:
                        # Преобразовываем значения в целые числа
                        sen1, sen2, sen3, sen4, sen5 = map(int, data)
                        # Вывод значений сенсоров в консоль
                        print(f"Значения сенсоров:")
                        print(f"  Сенсор 1: {sen1}")
                        print(f"  Сенсор 2: {sen2}")
                        print(f"  Сенсор 3: {sen3}")
                        print(f"  Сенсор 4: {sen4}")
                        print(f"  Сенсор 5: {sen5}")
                    except ValueError:
                        print(f"Ошибка при преобразовании данных: {line}")
                else:
                    print(f"Некорректный формат данных: {line}")

            # Задержка перед следующим циклом
            time.sleep(1)

        except KeyboardInterrupt:
            print("Программа завершена пользователем.")
            break
        
        except Exception as e:
            print(f"Ошибка: {e}")
            break

    ser.close()  # Закрываем соединение перед завершением программы

if __name__ == "__main__":
    main()

