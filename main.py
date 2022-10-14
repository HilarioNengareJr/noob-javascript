from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('helloworld.html')

@app.route('/variable')
def var():
    return render_template('variables.html')


@app.route('/function')
def funcs():
    return render_template("functions.html")

if __name__ == '__main__':
    app.run(debug=True)
