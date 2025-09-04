from flask import Flask,request,Response,url_for,session,redirect

app=Flask(__name__)
app.secret_key="supersecret"
@app.route("/",methods=["GET","POST"])
def login():
    if request.method=="POST":
           username=request.form.get("username")
           password = request.form.get("password")

           if username=="user" and password=="123":
                 session["user"]=username
                 return redirect(url_for("welcome"))
           else:
                 return Response("in valid credential\ntry again",mimetype="text/plain")
    return '''
         <h2>loginpage</h2>
         <form method="POST">
         username:<input type="text" name="username"><br>
         password:<input type="text" name="password"><br>
         <input type="submit" value="login">
         </form>

'''

@app.route("/welcome")
def welcome():
      if "user" in session:
            return f'''
                <h2>welcome,{session["user"]}!</h2>
                <a href={url_for('logout')}>logout</a>

            '''
      return redirect(url_for("login"))

@app.route("/logout")
def logout():
      session.pop("user", None)
      return redirect(url_for("login"))