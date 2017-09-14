from flask import Flask, render_template, redirect, request, session, flash
# import the Connector function
from mysqlconnection import MySQLConnector
import re, md5
password = 'password'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'logs_and_regs')
# an example of running a query
@app.route('/')
def index():

    query = "SELECT * FROM users"
    users = mysql.query_db(query)
    return render_template('index.html', all_emails=users)

@app.route('/form', methods=['POST'])
def create():

    query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
    # We'll then create a dictionary of data from the POST data received.
    password = md5.new(request.form['password']).hexdigest()
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'email': request.form['email'],
             'password': password
           }


    # verify if name fields are longer than 2 characters and do not contain numbers or special characters
    if len(request.form['first_name']) and len(request.form['last_name']) < 3:
        flash('*First and last name must be longer than 2 characters!')
        return redirect('/')
    elif not request.form['first_name'].isalpha():
        flash('*First and last name cannot contain numbers or special characters!')
        return redirect('/')

    # verify that email is not empty and is in valid format
    elif len(request.form['email']) < 1:
        flash("*Email cannot be blank!")
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("*Invalid Email Address!")
        return redirect('/')

    # verify if passwords are longer than 8 characters and match
    elif len(request.form['password']) < 8:
        flash('*Password must be at least 8 characters!')
        return redirect('/')
    elif request.form['password'] != request.form['verify_password']:
        flash('*Passwords do not match!')
        return redirect('/')

    else:
        mysql.query_db(query, data)
        return redirect('/success')


@app.route('/logIn', methods=['POST'])
def logIn():

    password = md5.new(request.form['log_password']).hexdigest()
    data = {
        'log_email': request.form['log_email'],
        'log_password': password
    }

    query = "SELECT * FROM users WHERE users.email = :log_email and users.password = :log_password"
    value = mysql.query_db(query, data)

    userId = "SELECT users.id FROM users WHERE users.email = :log_email"
    logged = mysql.query_db(userId, data)
    user_id = logged[0]['id']

    if len(value) < 1:
        flash("Email and password don't match")
        return redirect('/')
    else:
        #print logged
        session['user_logged_id'] = user_id
        session['logged_in'] = True
        print session['user_logged_id']
        print session['logged_in']
        return redirect('/success')

@app.route('/success')
def success():
    return render_template('success.html')

app.run(debug=True)
