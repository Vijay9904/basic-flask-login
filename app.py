from flask import Flask,request,redirect,url_for,session,Response
app=Flask(__name__)
app.secret_key="supersecret"
@app.route("/",methods=["GET","POST"])
#homepage login page
def login():
    if request.method=="POST":
       username = request.form.get("username")
       password = request.form.get("password")

       if username=="admin" and password=="123":
            session["user"]=username #store in session
            return redirect(url_for("welcome"))
       else:
            return Response("in-valid credentials,try again",mimetype="text/plain")

    return '''
             <h2>Login page</h2>
             <form method="POST">
             username:<input type="text" name="username"></br>
             password:<input type="text" name="password"></br>
             <input type="submit" value="Login">
              </form>
'''
@app.route("/welcome")
def welcome():
    if "user" in session:
        return f'''
                <h2>Welcome,{session["user"]}!</h2>
                <a href={url_for('logout')}>Logout</a>
'''
    return redirect(url_for("login"))
@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for("login"))

