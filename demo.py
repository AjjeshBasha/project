# print("Hello")
# print("Project 13")
# from flask import Flask,render_template,url_for
# app = Flask(__name__)

# @app.route('/')
# def demo():
#     return render_template('index.html')

# if __name__=='__main__':
#     app.run(debug=True)



import sqlite3
from flask import Flask,render_template,url_for,request
app = Flask(__name__)
@app.route('/')
def demo():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

conn = sqlite3.connect('team8.db')
print ("Opened database successfully")

#conn.execute('CREATE TABLE users (name TEXT, email TEXT, password TEXT)')
#print ("Table created successfully");
#conn.close()




@app.route("/signin",methods = ["POST","GET"])  
def signin():  
    msg = "msg"  
    if request.method == "POST":  
        try:  
            name = request.form["name"]  
            email = request.form["email"]  
            password = request.form["password"]  
            with sqlite3.connect("team8.db") as con:  
                cur = con.cursor()  
                cur.execute("INSERT into users (name, email, password) values (?,?,?)",(name,email,password))  
                con.commit()  
                msg = "User successfully Added"  
        except:  
            con.rollback()  
            msg = "We can not add the employee to the list"  
        finally:  
            return render_template("success.html",msg = msg)  
            con.close()
if __name__=='__main__':
    app.run(debug=True)