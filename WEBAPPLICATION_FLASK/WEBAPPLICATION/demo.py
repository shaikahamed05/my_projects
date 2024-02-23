from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import shutil
# from werkzeug import secure_filename
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
import mysql.connector
import sys
import glob
import numpy as np
import cv2
import sys
from datetime import date
from datetime import datetime
import smtplib

app = Flask(__name__)
db = mysql.connector.connect(host="localhost", username="root", password="", database="medical")


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/userregister')
def userregister():
    return render_template('registration.html')


@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')


@app.route('/feedback')
def feedback():
    return render_template('feedback.html')


@app.route('/userlogin')
def userlogin():
    return render_template('index.html')


@app.route('/UploadImage')
def UploadImage():
    return render_template('UploadImage.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/adminlogin')
def adminlogin():
    return render_template('inde.html')


@app.route('/addImagedb', methods=['GET', 'POST'])
def addImagedb():
    if os.path.exists('static/test/test.jpg'):
        os.remove('static/test/test.jpg')
    xx = []
    ress = ""
    cursor = db.cursor()
    uid = session['uid']
    sql1 = "SELECT userid,name,password,area,email,phno FROM users where userid='%s'" % (uid)
    rows_count1 = cursor.execute(sql1)
    data1 = cursor.fetchall()
    print(data1[0][4])
    if request.method == 'POST':
        f = request.files['photos']
        fname = f.filename
        ind = fname.index('.')
        fn = fname[ind:]

        print("current working directory ", os.getcwd())
        os.chdir("static/test")
        f.save(secure_filename("test.jpg"))

        cfname = "/static/test/" + str(fname)

        os.chdir('..')
        os.chdir('..')
        print("current working directory 2 ", os.getcwd())


@app.route('/userregisterdb', methods=['POST'])
def do_userregisterdb():
    uid = request.form['userid']
    name = request.form['name']
    email = request.form['email']
    phno = request.form['phno']
    area = request.form['area']
    password = request.form['password']

    cursor = db.cursor()
    cursor.execute('insert into users values("%s", "%s", "%s", "%s", "%s","%s")' % \
                   (uid, name, email, phno, area, password))
    db.commit()

    return render_template('index.html')


@app.route('/login', methods=['POST'])
def do_login():
    flag = False
    cursor = db.cursor()
    username = request.form['username']
    password = request.form['password']
    sql = "SELECT * FROM users WHERE userid= '%s' and password = '%s' " % (username, password)
    print("Sql  is ", sql)
    rows_count = cursor.execute(sql)
    if rows_count > 0:
        session['logged_in'] = True
        session['uid'] = username
        flag = True
    else:
        flag = False
    if flag:
        return render_template('userhome.html')
    else:
        return render_template('index.html')


# admin module starts

@app.route('/adminlogin', methods=['POST'])
def do_adminlogin():
    flag = False
    ##print ("Admin Login")
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'admin':
        session['logged_in'] = True
        flag = True
    else:
        flag = False
    if flag:
        return render_template('adminhome.html')
    else:
        return render_template('index.html')


@app.route('/viewfeedback')
def do_viewfeedbackdb():
    ##print ("Welcome feedback view")
    cursor = db.cursor()

    sql = "SELECT users.userid,name,feedback,date,time FROM users,feedback where users.userid=feedback.userid"
    rows_count = cursor.execute(sql)
    data = cursor.fetchall()
    if rows_count > 0:
        return render_template('viewfeedback.html', ddata=data)


@app.route('/viewadminfeedback')
def do_viewadminfeedbackdb():
    ##print ("Welcome feedback view")
    cursor = db.cursor()

    sql = "SELECT users.userid,name,feedback,date,time FROM users,feedback where users.userid=feedback.userid"
    rows_count = cursor.execute(sql)
    data = cursor.fetchall()
    if rows_count > 0:
        return render_template('viewadminfeedback.html', ddata=data)


@app.route('/profile')
def profiledb():
    cursor = db.cursor()
    uid = session['uid']

    sql = "SELECT userid,name,password,area,email,phno FROM users where userid='%s'" % (uid)
    rows_count = cursor.execute(sql)
    data = cursor.fetchall()
    if rows_count > 0:
        return render_template('profile.html', ddata=data)


@app.route('/viewusers')
def viewusersdb():
    cursor = db.cursor()

    sql = "SELECT userid,name,email,phno,area FROM users"
    rows_count = cursor.execute(sql)
    data = cursor.fetchall()
    if rows_count > 0:
        return render_template('viewusers.html', ddata=data)


@app.route('/userfeedbackdb', methods=['POST'])
def do_userfeedbackdb():
    userid = request.form['userid']
    feedback = request.form['feedback']
    today = date.today()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    cursor = db.cursor()
    cursor.execute('insert into feedback(userid,feedback,date,time) values("%s", "%s","%s","%s")' % \
                   (userid, feedback, today, current_time))
    db.commit()
    return render_template('userhome.html')


@app.route('/addplacesdb', methods=['POST'])
def do_addplacesdb():
    name = request.form['name']
    email = request.form['email']
    phno = request.form['phno']
    uname = request.form['username']
    password = request.form['password']
    cursor = db.cursor()
    cursor.execute('insert into patient values("%s", "%s", "%s", "%s", "%s")' % \
                   (name, email, phno, uname, password))
    db.commit()
    return render_template('patientlogin.html')


# admin module starts


# admin module Ends
@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()


if __name__ == "_main_":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0', port=8000)