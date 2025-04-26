from app import app


@app.route('/hello')
def hello():
    return "Hello, world!"


@app.route('/info')
def info():
    return "This is an informational page."


@app.route('/calc/<num1>/<num2>')
def calc(num1, num2):
    if not (num1.isdigit() and num2.isdigit()):
        return "Ошибка: оба параметра должны быть числами.", 400

    num1 = int(num1)
    num2 = int(num2)

    return f"The sum of {num1} and {num2} is {num1 + num2}."


@app.route('/reverse/', defaults={'string': ''})
@app.route('/reverse/<string>')
def reverse(string):
    if not string.strip():
        return "Ошибка: строка должна содержать хотя бы одни символ.", 400
    return reversed(string)


@app.route('/user/<name>/<age>')
def user(name, age):
    age = int(age)
    if age < 0:
        return "Ошибка: возраст не может быть отрицательным.", 400
    return f"Hello, {name}. You are {age} years old."
