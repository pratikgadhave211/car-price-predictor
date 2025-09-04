from flask import Flask,request


app=Flask(__name__)
@app.route("/")
def home():
    return "this is my first flask app"

@app.route("/about")
def about():
    return "this is about us page"

@app.route("/contact")
def contact():
    return "this is contact page"
      
@app.route("/submit",methods=["GET","POST"])
def submit():
    if request.method=="POST":
        return "you sent the data"
    else:
        return "you are just viewing the data"