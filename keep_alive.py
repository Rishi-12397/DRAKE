from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return 'DR1KE (932203120820379648) is alive!'

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()
