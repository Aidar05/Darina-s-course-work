from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='../FrontEnd/dist')

@app.route('/')
def main_page():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/static/<path:filename>')
def staticfiles(filename):
    return send_from_directory(app.static_folder, filename)

if __name__ == "__main__":
    app.run(debug=True)