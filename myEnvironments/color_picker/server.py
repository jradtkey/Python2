from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new', methods=['POST'])
def showColor():
    red = request.form['red']
    green = request.form['green']
    blue = request.form['blue']
    return redirect('/', red = red, green = green, blue = blue)

app.run(debug=True)
