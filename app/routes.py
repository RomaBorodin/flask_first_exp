from flask import render_template, request, flash, redirect, url_for
from app import app
from datetime import datetime


@app.route("/")
def home():
    current_time = datetime.now()
    return render_template("index.html", current_time=current_time)


@app.route("/about")
def about():
    team_members = [
        {'name': 'Alice', 'role': 'Developer'},
        {'name': 'Bob', 'role': 'Designer'},
        {'name': 'Charlie', 'role': 'Project Manager'}
    ]
    return render_template("about.html", team_members=team_members)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # обработка данных формы

        flash("Your message has been sent successfully")
        return redirect(url_for('contact'))

    support_info = {
        "name": "Анна Иванова",
        "position": "Менеджер по работе с клиентами",
        "email": "support@example.com",
        "address": {
            "street": "ул. Пушкина, д. 10",
            "city": "Москва",
            "zip": "101000"
        }
    }

    return render_template('contact.html', support=support_info)
