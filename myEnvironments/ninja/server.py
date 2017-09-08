from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/ninja')
def displayAll():
    return render_template('allNinjas.html')

@app.route('/ninja/<color>')
def showTurtle(color):
    if color == 'blue':
        return render_template('leo.html')
    elif color == 'purple':
        return render_template('don.html')
    elif color == 'red':
        return render_template('raph.html')
    elif color == 'orange':
        return render_template('mike.html')
    else:
        return render_template('april.html')
app.run(debug=True)
