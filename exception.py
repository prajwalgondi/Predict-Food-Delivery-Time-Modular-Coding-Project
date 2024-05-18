from flask import Flask
from FDTP.logger import logging
from FDTP.exception import CustomException
import os,sys

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    try:
        raise Exception('we aare testing exception file')
    except Exception as e:
        aml=CustomException(e,sys)
        logging.info(aml.error_message)
        logging.info("We are testing our logging file")

        return "Welcome to Prajwals world"

if __name__ == "__main__":
    app.run(debug = True) # 5000