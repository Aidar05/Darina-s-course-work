from flask import Flask, send_from_directory, request, redirect, session, url_for
from flask_cors import CORS
import mysql.connector
from db_logic import *

app = Flask(__name__, static_folder='../FrontEnd/dist')
CORS(app)
app.secret_key = 'eaa2cc52a16507cf194e4f0c'

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="gallery_data"
)

@app.route('/', methods=["POST", "GET"])
def main_page():
    return "Goodbye, World!"
    # return send_from_directory(app.static_folder, 'index.html')

@app.route('/sign-up', methods=['POST', 'GET'])
def sign_up():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form['password']
        add_user(db, username, email, password)

        # add_userData_toSession(username)

    return redirect(url_for("main_page"))

# def add_userData_toSession(login):
#   session['user_id'] = get_user_id(db, login)
#   user_data = get_user_data(db, session['user_id'])

#   session['logged_in'] = True
#   session['username'] = user_data[1]
#   session['email'] = user_data[2]
#   session['password'] = user_data[3]


@app.route('/static/<path:filename>')
def staticfiles(filename):
    return send_from_directory(app.static_folder, filename)

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5000)