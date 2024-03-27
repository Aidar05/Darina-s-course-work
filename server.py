from flask import Flask, render_template, request, session, redirect, url_for
import multiprocessing
import mysql.connector
from start_mysql import start_mysql 
from db_logic import *
from data import *
from modify_urls import *
from send_email import *

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
    user_id = get_user_id(db, 'username', username)
    
    save_to_liked(db, img_url, user_id)
    return 'saved'

@app.route('/works')
def works():
    return redirect(url_for('main_page', _anchor='works'))

@app.route('/sunflowers')
def sunflowers_section():
    return redirect(url_for('gallery', _anchor='sunflowers-series'))

@app.route('/van-gock')
def van_gock():
    return redirect(url_for('main_page', _anchor='Van-Gock-container'))

@app.route('/profile', methods=["POST", "GET"])
def get_profile_info():
    username = session['username']
    user_id = get_user_id(db, 'username', username)
    
    liked_urls_db = get_liked_urls(db, user_id)
    liked_urls = filter_liked(liked_urls_db)

    return render_template(
        'profile.html',
        username = session['username'],
        email = session['email'],
        password = session['password'],
        liked_urls = liked_urls
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

@app.route('/recovery', methods=['POST', 'GET'])
def password_recovery():
    if request.method == "GET":
        return render_template('password_recovery.html')
    elif request.method == "POST":
        email = request.form["email"] 
        token = generate_token(email)
        send_email(email, token)
        return redirect(url_for('login'))
    
@app.route('/change_password', methods={"POST", "GET"})
def change_password():
    if request.method == 'GET':
        return render_template('change_password.html')
    elif request.method == "POST":
        email = request.form["email"]
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']

        if new_password == confirm_password:
            user_id = get_user_id(db, column_name='email', value=email)
            change_user_password(db, user_id, new_password)

            return redirect(url_for('login'))
        return render_template('change_password.html')

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