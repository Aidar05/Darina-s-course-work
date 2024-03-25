from flask import Flask, render_template, request, session, redirect, url_for
import multiprocessing
import mysql.connector
from start_mysql import start_mysql 
from db_logic import *
from data import *
from modify_urls import *

app = Flask(__name__)
app.secret_key = 'eaa2cc52a16507cf194e4f0c'


@app.route('/')
def main_page():
    create_table(db)
    return render_template('index.html')

@app.route('/gallery', methods=["GET"])
def gallery():
    template_data = {
        'self_portraits': self_portraits,
        'sunflowers': sunflowers,
        'arl_works': arl_works,
        'author_copies': author_copies
    }
    
    if 'username' in session:
        template_data['username'] = session['username']
    
    return render_template('gallery.html', **template_data)

@app.route('/like_dislike', methods=['POST'])
def like_dislike():
    img_url = request.data.decode('utf-8')
    username = session['username']
    user_id = get_user_id(db, username)
    
    save_to_liked(db, img_url, user_id)
    return 'saved'

@app.route('/works')
def works():
    return redirect(url_for('main_page', _anchor='works'))

@app.route('/van-gock')
def van_gock():
    return redirect(url_for('main_page', _anchor='Van-Gock-container'))

@app.route('/profile', methods=["POST", "GET"])
def get_profile_info():
    user_id= get_user_id(db, session['username'])
    # liked = get_liked_urls(db, user_id)[0].split()
    print(liked)
    # liked = filter_liked(liked)
    print(liked)

    return render_template(
        'profile.html',
        username = session['username'],
        email = session['email'],
        password = session['password'],
        # liked = liked
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