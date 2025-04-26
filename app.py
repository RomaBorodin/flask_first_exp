from flask import Flask

app = Flask(__name__)


# 1
@app.route('/hello')
def hello():
    return "Hello, world!"


@app.route('/info')
def info():
    return "This is an informational page."


# 2
@app.route('/calc/<num1>/<num2>')
def calc(num1, num2):
    if not (num1.isdigit() and num2.isdigit()):
        return "Ошибка: оба параметра должны быть числами.", 400

    num1 = int(num1)
    num2 = int(num2)

    return f"The sum of {num1} and {num2} is {num1 + num2}."


# 3
@app.route('/reverse/', defaults={'string': ''})
@app.route('/reverse/<string>')
def reverse(string):
    if not string.strip():
        return "Ошибка: строка должна содержать хотя бы одни символ.", 400
    return reversed(string)


# 4
@app.route('/user/<name>/<age>')
def user(name, age):
    age = int(age)
    if age < 0:
        return "Ошибка: возраст не может быть отрицательным.", 400
    return f"Hello, {name}. You are {age} years old."


if __name__ == "__main__":
    app.run(debug=True)
