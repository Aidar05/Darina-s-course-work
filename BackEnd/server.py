from flask import Flask

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def main_page():
  return "Goodbye World!"