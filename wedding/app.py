from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('init.html')

@app.route('/fc')
def hello_world():
    return 'Fastcampus!'

if __name__ == '__main__':
    app.run()