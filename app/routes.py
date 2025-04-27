from flask import render_template, request, redirect, url_for
from app import app


@app.route("/")
def form():
    return render_template("form.html")


@app.route("/submit", methods=["POST", "GET"])
def submit():
    if request.method == "POST":
        data = {
            "name": request.form.get("name"),
            "email": request.form.get("email"),
            "color": request.form.get("color"),
            "profession": request.form.get("profession"),
            "hobbies": request.form.getlist("hobbies"),
            "level": request.form.get("level"),
        }

        return render_template("result.html", **data)
    return redirect(url_for("form"))


@app.route("/result")
def result():
    return render_template("result.html")
