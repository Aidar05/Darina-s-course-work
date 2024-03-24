from flask import Flask, render_template, request, session, redirect, url_for
from db_logic import *
import os
import mysql.connector

app = Flask(__name__)
app.secret_key = 'eaa2cc52a16507cf194e4f0c'

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="gallery_data"
)

@app.route('/')
def main_page():
    print(session)
    return render_template('index.html')

@app.route('/gallery', methods=["GET"])
def gallery():
    portrait_url = 'gallery/self_portraits/self_portrait'
    sunflower_url = 'gallery/block2/sunflowers'
    self_portraits = [
        {
        'img_info': 'Self-Portrait in front of the Easel',
        'dimens': '1888 (200 Kb); 65 x 50.5 cm',
        'url': url_for('static', filename=f'{portrait_url}.png')
        },
        {
        'img_info': 'Self-Portrait in front of the Easel',
        'dimens': '1888 (200 Kb); 65 x 50.5 cm',
        'url': url_for('static', filename=f'{portrait_url}2.png')
        },
        {
        'img_info': 'Self-Portrait in front of the Easel',
        'dimens': '1888 (200 Kb); 65 x 50.5 cm',
        'url': url_for('static', filename=f'{portrait_url}3.png')
        },
        {
        'img_info': 'Self-Portrait in front of the Easel',
        'dimens': '1888 (200 Kb); 65 x 50.5 cm',
        'url': url_for('static', filename=f'{portrait_url}4.png')
        },
        {
        'img_info': 'Self-Portrait in front of the Easel',
        'dimens': '1888 (200 Kb); 65 x 50.5 cm',
        'url': url_for('static', filename=f'{portrait_url}5.png')
        }
    ]
    sunflowers = [
        {
        'img_info': 'Self-Portrait in front of the Easel',
        'dimens': '1888 (200 Kb); 65 x 50.5 cm',
        'url': url_for('static', filename=f'{sunflower_url}1.png')
        },
        {
        'img_info': 'Self-Portrait in front ofs the Easel',
        'dimens': '1888 (200 Kb); 65 x 50.5 cm',
        'url': url_for('static', filename=f'{sunflower_url}2.png')
        },
        {
        'img_info': 'Self-Portrait in front of the Easel',
        'dimens': '1888 (200 Kb); 65 x 50.5 cm',
        'url': url_for('static', filename=f'{sunflower_url}3.png')
        },
        {
        'img_info': 'Self-Portrait in front of the Easel',
        'dimens': '1888 (200 Kb); 65 x 50.5 cm',
        'url': url_for('static', filename=f'{sunflower_url}4.png')
        },
    ]
    return render_template(
        'gallery.html',
        self_portraits=self_portraits,
        sunflowers=sunflowers
    )

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
    app.run(host='0.0.0.0', port='43345', debug=True)