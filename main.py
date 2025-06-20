from flask import Flask,render_template,request,session
from database import Database
from myapi import Api
app=Flask(__name__)

#key for session
app.secret_key="hithisissingh9103414128"

#objects for classes
db=Database()
ap=Api()

#main
@app.route("/")
def login():
    return render_template("login.html")

#about
@app.route("/about")
def about():
    return render_template("about.html")


#logout
@app.route("/logout")
def logout():
    session.clear()
    return render_template("login.html")

#register
@app.route("/register")
def register():
    return render_template("register.html")

#doing registration
@app.route("/perform_reg",methods=["post"])
def perform_registration():
    name=request.form.get("user_name")
    email=request.form.get("user_email")
    password=request.form.get("user_password")
    
    response=db.add_data(name,email,password)
    
    return render_template("login.html",message=response)   

#doing login
@app.route("/perform_login",methods=["post"])
def perform_login():
    email=request.form.get("user_email")
    password=request.form.get("user_password")
    
    response=db.search_data(email,password)
    if response == "Login succesful":
        name = session["user_name"]
        return render_template("home.html", message=response, name=name, selected_analysis="sentiment")
    else:
        return render_template("login.html", message=response)

#home
@app.route("/home")
def home_page():
    if "user_name" in session:
        name=session["user_name"]
        return render_template("home.html",name=name, selected_analysis="sentiment")
    else:
        return render_template("login.html",message="Please Login First")
            
#sentiment
@app.route("/analyze/sentiment",methods=["Post"])
def sentiment():
    if "user_name" not in session:
        return render_template("login.html", message="Please login first")
    try:
        text=request.form.get("sentiment")
        if not text.strip():
            return render_template("home.html",noresult="Please enter the text",selected_analysis="sentiment")
        else:
            response=ap.sentiment(text)
            return render_template("home.html",result=response, selected_analysis="sentiment")
    except Exception as e:
        return render_template("home.html",noresult="Some Error occur", selected_analysis="sentiment")
    

#ner
@app.route("/ner",methods=["Post"])
def ner():
    if "user_name" not in session:
        return render_template("login.html", message="Please login first")
    try:
        text=request.form.get("ner")
        if not text.strip():
            return render_template("home.html", noresult_ner="Please enter the text" ,selected_analysis="ner")
        else:
            response=ap.ner(text)
            return render_template("home.html", result_ner=response,selected_analysis="ner")
    except Exception as e:
        return render_template("home.html", noresult_ner="Some error occur", selected_analysis="ner")

#emotion
@app.route("/emotion",methods=["Post"])
def emotion():
    if "user_name" not in session:
        return render_template("login.html", message="Please login first")
    try:
        text=request.form.get("emotion")
        if not text.strip():
            return render_template("home.html", noresult_emotion="Please enter the text" ,selected_analysis="emotion")
        else:
            response=ap.emotion(text)
            
            if isinstance(response, list) and len(response) == 1 and isinstance(response[0], list):
                response = response[0]
            return render_template("home.html", result_emotion=response, selected_analysis="emotion")

        
    except Exception as e:
        return render_template("home.html", noresult_emotion="Some Error occur" ,selected_analysis="emotion")
        
        
#summary
@app.route("/summary", methods=["POST"])
def summary():
    if "user_name" not in session:
        return render_template("login.html", message="Please login first")
    try:
        text=request.form.get("summary")
        if not text.strip():
            return render_template("home.html", noresult_summary="Please enter the text", selected_analysis="summary")
        else:
            response=ap.summarizerapi(text)
            response=response[0]["summary_text"]
            print("api hit")
            return render_template("home.html", result_summary=response, selected_analysis="summary")
            
    except Exception as e:
        return render_template("home.html", noresult_summary="Some Error occur", selected_analysis="summary")
            
        
    



app.run(debug=True)