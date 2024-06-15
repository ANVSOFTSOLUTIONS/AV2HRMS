from flask import Flask,render_template,request,redirect,url_for
from flask_mysqldb import MySQL
app = Flask(__name__)
app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']="registration"
mysql = MySQL(app)
@app.route("/", methods=["POST", "GET"])
def Contact():
    if request.method=="POST":
      email=request.form["email"]
      username=request.form["uname"]
      fname=request.form["fname"]
      lname=request.form["lname"]
      Password=request.form["pass"]
      confirm_pass=request.form["confirm_pass"]
      cur=mysql.connection.cursor()
      cur.execute("INSERT INTO user_registration(email,username,fname,lname,Password,confirm_pass)VALUES(%s,%s,%s,%s,%s,%s)",(email,username,fname,lname,Password,confirm_pass))
      mysql.connection.commit()
      cur.close()
      return("success" )
    return render_template("loginpage.html") 

if __name__ == '__main__':
  app.run(debug=True)