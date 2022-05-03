from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>URL Bot Is Running </h1>"

def run():
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)

def keep_alive():
	t = Thread(target = run)
	t.start()