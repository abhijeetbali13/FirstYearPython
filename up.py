from flask import Flask, render_template, request, session, redirect, url_for
from functools import wraps
from database import Database
from myapi import Api

app = Flask(__name__)
app.secret_key = "hithisissingh9103414128"

db = Database()
ap = Api()

# Decorator to restrict access to logged-in users
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_name" not in session:
            return redirect(url_for("login", message="Please login first"))
        return f(*args, **kwargs)
    return decorated_function


@app.route("/")
def login():
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return render_template("login.html", message="Logged out successfully")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/perform_reg", methods=["POST"])
def perform_registration():
    name = request.form.get("user_name")
    email = request.form.get("user_email")
    password = request.form.get("user_password")

    response = db.add_data(name, email, password)
    return render_template("login.html", message=response)


@app.route("/perform_login", methods=["POST"])
def perform_login():
    email = request.form.get("user_email")
    password = request.form.get("user_password")

    response = db.search_data(email, password)

    if response == "Login succesful":
        name = session["user_name"]
        return render_template("home.html", message=response, name=name)
    else:
        return render_template("login.html", message=response)


@app.route("/home")
@login_required
def home_page():
    name = session["user_name"]
    return render_template("home.html", name=name)


@app.route("/analyze/sentiment", methods=["POST"])
@login_required
def sentiment():
    text = request.form.get("sentiment")
    name = session["user_name"]

    if not text.strip():
        return render_template("home.html", noresult="Please enter the text", name=name)

    response = ap.sentiment(text)
    return render_template("home.html", result=response, name=name)


# Optional (future support if needed)
@app.route("/analyze/ner", methods=["POST"])
@login_required
def ner():
    text = request.form.get("ner")
    name = session["user_name"]
    # Dummy logic, replace with real implementation later
    result = {"entities": ["Example Entity"]}
    return render_template("home.html", ner_result=result, name=name)


@app.route("/analyze/emotion", methods=["POST"])
@login_required
def emotion():
    text = request.form.get("emotion")
    name = session["user_name"]
    # Dummy logic, replace with real implementation later
    result = {"emotion": "Happy"}
    return render_template("home.html", emotion_result=result, name=name)


@app.route("/analyze/summary", methods=["POST"])
@login_required
def summary():
    text = request.form.get("summary")
    name = session["user_name"]
    # Dummy logic, replace with real implementation later
    result = {"summary": "This is a summary."}
    return render_template("home.html", summary_result=result, name=name)


if __name__ == "__main__":
    app.run(debug=True)
