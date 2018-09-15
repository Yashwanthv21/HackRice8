#!/usr/bin/python

from flask import Flask, jsonify, request, abort, render_template
import json

app = Flask(__name__)


@app.route('/home')
def devices():
    return render_template('home.html')

@app.route('/about')
def about():
    return 'The about page'


# @app.after_request
# def after_request(response):
#     response.headers.add('Content-Type', 'application/json')
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     response.headers.add('Access-Control-Allow-Headers',
#                          'Content-Type,Authorization')
#     response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
#     return response


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, threaded=False)
