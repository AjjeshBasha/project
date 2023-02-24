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
from flask import Flask,redirect,url_for,render_template,request,session
def register_user_to_db(name,email,password):
    con=sqlite3.connect('team8.db')
    cur=con.cursor()
    cur.execute('INSERT INTO users(name,email,password)values(?,?,?)',(name,email,password))
    con.commit()
    con.close()


def check_user(email,password):
    con=sqlite3.connect('team8.db')
    cur=con.cursor()
    cur.execute('Select email,password FROM users WHERE email=? and password=?',(email,password))

    result=cur.fetchone()
    if result:
        return True
    else:
        return False    
app = Flask(__name__)
app.secret_key="random"


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/savedetails",methods=["POST","GET"])
def savedetails():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        password=request.form['password']

        register_user_to_db(name,email,password)
        return redirect(url_for('index'))

    else:
        return render_template('index.html')

@app.route("/valid_login",methods=["POST","GET"])
def valid_login():
    if request.method=='POST':
        email=request.form['email']
        password=request.form['password']

        if check_user(email,password):
            session['email']=email
        
        return redirect(url_for('home'))

    else:
        redirect(url_for('wrong'))
@app.route('/home',methods=["POST","GET"])
def home():
    if 'email' in session:
        return render_template('home.html',email=session['email'])
    else:
        return render_template('wrong.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
if __name__=='__main__':
    app.run(port=2022,debug=True)
    print(yes)