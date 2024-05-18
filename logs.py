from flask import Flask
from FDTP.logger import logging

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    logging.info("We are testing our logging file")

    return "Welcome to Prajwals world"

if __name__ == "__main__":
    app.run(debug = True) # 5000