from flask import Flask, render_template, jsonify, request
import serial
import time
app = Flask(__name__)
# Главная страница
@app.route('/')
def home():
    return render_template('index.html')

# Генерация случайных значений
@app.route('/get_values')
def get_values():
    PORT = "/dev/ttyACM0"
    BAUD_RATE = 9600
    sen1 = sen2 = sen3 = sen4 = sen5 = 0

    ser = serial.Serial(PORT, BAUD_RATE, timeout=1)
    print(f"Соединение установлено на {PORT} со скоростью {BAUD_RATE}")
    time.sleep(2)  # Даем время на инициализацию Serial

    while True:
        # Если Arduino отправляет данные, считываем строку
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').strip()  # Считываем строку
            metrix = data.split(",")
            if len(metrix) == 5:
                sen1, sen2, sen3, sen4, sen5 = map(int, metrix)

        # Передаем полученные значения с Arduino
        values = {
            "sen1": sen1,
            "sen2": sen2,
            "sen3": sen3,
            "sen4": sen4,
            "sen5": sen5,
        }
        return jsonify(values)
#Передаем Arduino команду на обнуление значений
@app.route('/reset_to_zero', methods=['POST','GET'])
def reset_to_zero():
    PORT = "/dev/ttyACM0"
    BAUD_RATE = 9600
    try:
        ser = serial.Serial(PORT, BAUD_RATE, timeout=1)
        command = request.args.get('command', 'c')
        ser.write(command.encode())  # Отправляем команду
        print(f"Отправлена команда: {command}")
        return 'Браво-6, принял!', 200  # Возврат строки с HTTP-кодом 200
    except Exception as e:
        print(f"Ошибка отправки команды: {e}")
        return f"Произошла ошибка: {str(e)}", 500 #Bravo 6 going dark
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

