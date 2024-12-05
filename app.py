from flask import Flask, render_template, jsonify, request
import serial
import time

app = Flask(__name__)

# Глобальная инициализация порта
PORT = "/dev/ttyACM0"
BAUD_RATE = 9600
ser = serial.Serial(PORT, BAUD_RATE, timeout=1)  # Открываем порт один раз
time.sleep(2)  # Даем время Arduino инициализироваться

# Главная страница
@app.route('/')
def home():
    return render_template('index.html')

# Получение данных с Arduino
@app.route('/get_values')
def get_values():
    global ser
    try:
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').strip()
            print(f"Получены данные: {data}")
            metrix = data.split(",")
            if len(metrix) == 5:
                try:
                    sen1, sen2, sen3, sen4, sen5 = map(int, metrix)
                except ValueError:
                    print(f"Ошибка при обработке: {data}")
                    sen1 = sen2 = sen3 = sen4 = sen5 = 0
            else:
                sen1 = sen2 = sen3 = sen4 = sen5 = 0
        else:
            sen1 = sen2 = sen3 = sen4 = sen5 = 0

        values = {
            "sen1": sen1,
            "sen2": sen2,
            "sen3": sen3,
            "sen4": sen4,
            "sen5": sen5,
        }
        return jsonify(values)

    except Exception as e:
        print(f"Ошибка при чтении данных: {e}")
        return jsonify({"error": str(e)})

# Обнуление значений на Arduino
@app.route('/reset_to_zero', methods=['POST', 'GET'])
def reset_to_zero():
    global ser
    try:
        command = request.args.get('command', 'c')
        ser.write(command.encode())
        print(f"Отправлена команда: {command}")
        return jsonify({"message": "Команда отправлена успешно"}), 200
    except Exception as e:
        print(f"Ошибка: {e}")
        return jsonify({"error": str(e)}), 500

# Запуск приложения
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

