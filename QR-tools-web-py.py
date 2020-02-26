from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    # return "Hello Flask"
    return render_template('index.html')

@app.route('/sayhello')
def sayhello():
    return render_template('sayhello.html', name='vigo')

@app.route('/login')
def login():
    return "wellcom to login!"

if __name__ == '__main__':
    app.run(debug=True, port=8080)