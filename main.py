import flask
from flask_cors import CORS, cross_origin
from flask import Flask, request


app = Flask(__name__)
CORS(app)


if __name__ == '__main__':
    print('hello world')
    app.run(debug=True)

