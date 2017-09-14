from flask import Flask, render_template, redirect, request, session, flash
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'email_verification')
# an example of running a query
@app.route('/')
def index():
    query = "SELECT * FROM emails"                           # define your query
    emails = mysql.query_db(query)                           # run query with query_db()
    return render_template('index.html', all_emails=emails)

@app.route('/emails', methods=['POST'])
def create():

    verification = "SELECT * FROM emails WHERE email_verificationcol = :email"

    data = {
            'email': request.form['email'],
           }
    check = len(mysql.query_db(verification, data))

    if check > 0:
        flash('Email already exists')
        return redirect('/')
    else:
        query = "INSERT INTO emails (email_verificationcol, created_at) VALUES (:email, NOW())"
        mysql.query_db(query, data)
        return redirect('/')




app.run(debug=True)
