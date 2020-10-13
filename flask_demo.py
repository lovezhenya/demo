from flask import jsonify
from flask import Flask
from flask import request
from collections import OrderedDict
import os
import sys
from gevent import monkey
monkey.patch_all()

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def get_text_input():
    return "哈哈"
if __name__ == "__main__":   
    app.config['JSON_AS_ASCII'] = False
    app.run(host='127.0.0.1',port=5002)