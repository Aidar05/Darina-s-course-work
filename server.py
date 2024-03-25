from flask import Flask, render_template, request, session, redirect, url_for
import multiprocessing
from start_mysql import start_mysql 
import mysql.connector
from db_logic import *
from data import *

app = Flask(__name__)
app.secret_key = 'eaa2cc52a16507cf194e4f0c'

@app.route('/')
def main_page():
    print(session)
    return render_template('index.html')

@app.route('/gallery', methods=["GET"])
def gallery():
    return render_template(
        'gallery.html',
        self_portraits=self_portraits,
        sunflowers=sunflowers,
        arl_works=arl_works,
        author_copies=author_copies
    )

@app.route('/like_dislike', methods=['POST'])
def like_dislike():
    print(request.data.decode('utf-8'))
    return 'liked'

@app.route('/works')
def works():
    return redirect(url_for('main_page', _anchor='works'))

@app.route('/van-gock')
def van_gock():
    return redirect(url_for('main_page', _anchor='Van-Gock-container'))

@app.route('/profile', methods=["POST", "GET"])
def get_profile_info():     
    return render_template(
        'profile.html',
        username = session['username'],
        email = session['email'],
        password = session['password'],
    )

@app.route('/sign-up', methods=['POST', 'GET'])
def registration():
    if request.method == "GET":
        return render_template("sign-up.html")
    
    elif request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form['password']
        add_user(db, username, email, password)

        session['username'] = username
        session['email'] = email
        session['password'] = password

        return redirect(url_for("main_page"))

@app.route('/sign-in', methods=['POST', 'GET'])
def login():
    if request.method == "GET":
        return render_template("sign-in.html")

    elif request.method == "POST":
        # Может быть либо именем либо почтой
        username = request.form["username"]  
        email = get_userColumn_byUsername(db, username, 'email')
        password = request.form['password']   
    
        if check_user(db, username, password)[0]:
            session['username'] = username
            session['password'] = password
            session['email'] = email
            return redirect(url_for("main_page"))
        else: 
            return render_template("sign-in.html")

@app.route('/log-out')
def logout():
    session.clear()
    return redirect(url_for('main_page'))

if __name__ == '__main__':
    p = multiprocessing.Process(target=start_mysql)
    p.start()

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="gallery_data"
    )
    
    app.run(host='0.0.0.0', port='43345', debug=True)