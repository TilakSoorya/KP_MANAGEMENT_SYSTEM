from flask import render_template, request, redirect, url_for,flash
from app import app, student
import re
import time

def is_valid_email(email_address):
   match = re.match(r"^[a-zA-Z0-9]{1,10}+@[a-zA-Z0-9]{1,5}+\.[a-z]{1,3}$", email_address)
   return True


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

# @app.route('/faultreport')
# def report():
#     return render_template('.html')

@app.route('/sign')
def sign():
    return render_template('signup.html')


@app.route('/store', methods=['POST','GET'])
def store_data():
    roll = request.form['roll']
    email = request.form['email']
    deg = request.form['degree']
    course = request.form['course']
    year = request.form['year']
    password = request.form['pass']
    cpass = request.form['cpass']

    if (roll =='' or email == '' or deg =='' or course =='' or year=='' or password == '' or cpass== ''):
        return render_template('signup.html',msg='Please Fill All the Fields!!')
    elif len(roll)!= 10:
        return render_template('signup.html',msg='Invalid Roll Number!!')
    # elif is_valid_email(email):
    #     return render_template('signup.html',msg='Enter a Valid Email!!')
    elif cpass!=password:
        return render_template('signup.html',msg='Password and Confirm Password are not save!')
    else:
        usr = student.find_one({'roll' :roll})
        if usr:
            return render_template('signup.html',msg='User Already Exists!!')
        else:
            student.insert_one({'roll': roll, 'email': email,'degree':deg,'course':course,'year':year,'password':password})
            return render_template('index.html')
        

@app.route('/studlog', methods = ['POST','GET'])
def login():
    email = request.form['email']
    pswd = request.form['pass']
    res = student.find_one({'email':email,'password':pswd})
    if res:
        return render_template('gridview.html',msg='',msg2="Login Successful!!",formno="form1")
    else:
        return render_template('index.html',msg="Invalid Credentials",msg2='',formno="form1")

