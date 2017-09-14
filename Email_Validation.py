from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
import datetime
app = Flask(__name__)
mysql = MySQLConnector(app,'email_vali')
app.secret_key = 'codingdojo'

@app.route('/')
def index():
  # query = "SELECT * FROM email_adress"
  # email_adress = mysql.query_db(query)
  return render_template('Email_Validation.html')

@app.route('/email', methods = ['POST'])
def displayemail():
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    
    if not EMAIL_REGEX.match(request.form['email_input']):
      flash('Invalid email address!')
      return redirect('/')
    else:
      query = "INSERT INTO email_adress (email) VALUES (:email)"
      data = {
            'email': request.form['email_input']
           }
      show_email = mysql.query_db(query, data)
      return redirect('/success')

@app.route('/success')
def successpost():
    query = "SELECT email FROM email_adress"
    show_email = mysql.query_db(query)
    return render_template('success.html', allemail = show_email)


app.run(debug=True)
