import os
from flask import Flask, request, render_template, redirect
from flask.json import jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/local"
mongo = PyMongo(app)

@app.route('/make')
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)