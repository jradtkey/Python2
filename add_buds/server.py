from flask import Flask, render_template, redirect, request, session, flash
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'mydb')
# an example of running a query
@app.route('/')
def index():
    query = "SELECT * FROM users"                           # define your query
    users = mysql.query_db(query)                           # run query with query_db()
    return render_template('index.html', all_friends=users)

@app.route('/users', methods=['POST'])
def create():
    # Write query as a string. Notice how we have multiple values
    # we want to insert into our query.
    query = "INSERT INTO users (name, age, created_at) VALUES (:name, :age, NOW())"
    # We'll then create a dictionary of data from the POST data received.
    data = {
            'name': request.form['name'],
            'age':  request.form['age'],
           }
    # Run query, with dictionary values injected into the query.
    mysql.query_db(query, data)
    return redirect('/')


app.run(debug=True)
