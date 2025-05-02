from flask import render_template, request, flash, redirect, url_for
from app import app


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # обработка данных формы

        flash("Your message has been sent successfully")
        return redirect(url_for('contact'))

    return render_template('contact.html')
