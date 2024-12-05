from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Главная страница
@app.route('/')
def home():
    return render_template('index.html')

# Генерация случайных значений
@app.route('/random_values')
def random_values():
    # Генерируем рандомные значения для 5 сенсоров
    values = {
        "sen1": random.randint(1, 100),
        "sen2": random.randint(1, 100),
        "sen3": random.randint(1, 100),
        "sen4": random.randint(1, 100),
        "sen5": random.randint(1, 100),
    }
    return jsonify(values)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


