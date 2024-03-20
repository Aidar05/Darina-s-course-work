from flask import Flask, send_from_directory, request, redirect, session, url_for
import mysql.connector
from db_logic import *

app = Flask(__name__, static_folder='../FrontEnd/dist')
app.secret_key = 'eaa2cc52a16507cf194e4f0c'

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="gallery_data"
)

@app.route('/')
def main_page():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('sign-up', methods=['POST', 'GET'])
def sign_up():
    if request.method == "GET":
        return redirect("sign-up.html")
    
    elif request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form['password']
        add_user(db, username, email, password)

        add_userData_toSession(username)

        return redirect(url_for("main_page"))

def add_userData_toSession(login):
  session['user_id'] = get_user_id(db, login)
  user_data = get_user_data(db, session['user_id'])

  session['logged_in'] = True
  session['username'] = user_data[1]
  session['email'] = user_data[2]
  session['password'] = user_data[3]
  session['history'] = user_data[4]


@app.route('/static/<path:filename>')
def staticfiles(filename):
    return send_from_directory(app.static_folder, filename)

if __name__ == "__main__":
    app.run(debug=True)