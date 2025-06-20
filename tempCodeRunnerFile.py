@app.route("/perform_reg",methods=["post"])
def perform_registration():
    name=request.form.get("user_name")
    email=request.form.get("user_email")
    password=request.form.get("user_password")
    
    response=db.add_data(name,email,password)
    
    return render_template("login.html",message=response)
    
    
    
    

@app.route("/perform_login",methods=["post"])
def perform_login():
    email=request.form.get("user_email")
    password=request.form.get("user_password")
    
    response=db.search_data(email,password)
    
    return render_template("home.html",message=response)
