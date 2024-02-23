import random
import smtplib
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql
from verify_email import verify_email

def signup():
    def emailid_enter(event):
        if emailidEntry.get() == 'Email ID':
            emailidEntry.delete(0, END)
            emailidEntry.config(width=35, bd=0, bg='white', fg='black')


    def send_otp():

        emailid = str(emailidEntry.get())
        emailidcheck=str(verify_email(emailid))

        try:
            con = pymysql.connect(host='localhost',
                                  user='root',
                                  password=''
                                  )
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Database Connectivity Issue Pls Try again')
            return

        try:
            query = 'create database emol'
            mycursor.execute(query)
            query = 'use emol'
            mycursor.execute(query)
            query = 'create table users_data(id int auto_increment primary key not null,email_id varchar(100),username varchar(100), password varchar(30))'
            mycursor.execute(query)
        except:
            mycursor.execute('use emol')

        query = 'select * from users_data where email_id =%s'
        mycursor.execute(query, emailid)
        row = mycursor.fetchone()
        if row != None:
                messagebox.showerror('Error', 'Username Already Exists')
        else:
            if True:
                if emailidcheck=='True':
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login('emobotpsender@gmail.com', 'bvksbebimbmmjfbs')
                    otp = ''.join(([str(random.randint(0, 9)) for i in range(6)]))
                    OTP = str(otp)
                    SUBJECT='emol OTP to Verify:'
                    TEXT=OTP + ' Is Your emol Verification Code'
                    msg='Subject: {}\n\n{}'.format(SUBJECT,TEXT)
                    server.sendmail('emobotpsender@gmail.com', emailid, msg)
                    server.quit()
                    emailverification.destroy()

                    def otp_enter(event):
                        if otpEntry.get() == 'Enter the OTP':
                            otpEntry.delete(0, END)
                            otpEntry.config(width=12, bd=0, bg='white', fg='black')

                    def verify_otp():
                        otp1 = otpEntry.get()
                        if otp1 == OTP:
                            messagebox.showinfo('Verified', 'Your Email is Verified Seccussfuly:')
                            enterotp.destroy()

                            def connect_database():
                                if usernameEntry.get() == '' or passwordEntry.get() == '' or confirmpasswordEntry.get() == '':
                                    messagebox.showerror('Error', 'All Fields Are Required')
                                elif passwordEntry.get() != confirmpasswordEntry.get():
                                    messagebox.showerror('Error', 'Password mismatch Error')
                                else:
                                    mycursor.execute('use emol')

                                    query = 'select * from users_data where username=%s'
                                    mycursor.execute(query, (usernameEntry.get()))
                                    row = mycursor.fetchone()
                                    if row != None:
                                        messagebox.showerror('Error', 'Username Already Exists')
                                    else:
                                        query = 'insert into users_data(email_id,username,password) values(%s,%s,%s)'
                                        mycursor.execute(query, (emailid,usernameEntry.get(), passwordEntry.get()))
                                        con.commit()
                                        con.close()
                                        messagebox.showinfo('Success', 'Registration is successful')
                                        signup_window.destroy()
                                        from LOGIN2 import Login
                                        Login()

                            def user_enter(event):
                                if usernameEntry.get() == 'Username':
                                    usernameEntry.delete(0, END)
                                    usernameEntry.config(width=35, bd=0, bg='white', fg='black')

                            def password_enter(event):
                                if passwordEntry.get() == 'Password':
                                    passwordEntry.delete(0, END)
                                    passwordEntry.config(width=35, bd=0, bg='white', fg='black')

                            def confirmpassword_enter(event):
                                if confirmpasswordEntry.get() == 'confirm Password':
                                    confirmpasswordEntry.delete(0, END)
                                    confirmpasswordEntry.config(width=35, bd=0, bg='white', fg='black')

                            def hide():
                                hideButton.config(image=open_eye, bd=0, bg='white', fg='gray50', cursor='hand2')
                                passwordEntry.config(show='*')
                                hideButton.config(command=show)

                            def show():
                                hideButton.config(image=close_eye, bd=0, bg='white', fg='gray50', cursor='hand2')
                                passwordEntry.config(show='')
                                hideButton.config(command=hide)

                            def hide1():
                                hideButton1.config(image=open_eye, bd=0, bg='white', fg='gray50', cursor='hand2')
                                confirmpasswordEntry.config(show='*')
                                hideButton1.config(command=show1)

                            def show1():
                                hideButton1.config(image=close_eye, bd=0, bg='white', fg='gray50', cursor='hand2')
                                confirmpasswordEntry.config(show='')
                                hideButton1.config(command=hide1)

                            signup_window = Tk()
                            signup_window.geometry('1366x768')
                            signup_window.title('signup page')
                            bgImage = ImageTk.PhotoImage(file='Images/EMOD_BG_for_login_page_1.jpg')
                            signup_window.state('zoomed')

                            close_eye = PhotoImage(file='Images/close_eye.png')
                            open_eye = PhotoImage(file='Images/open_eyes.png')

                            bglabel = Label(signup_window, image=bgImage)
                            bglabel.place(x=0, y=0)

                            heading = Label(signup_window, text='CREATE YOUR ACCOUNT',
                                            font=('arial', 20, 'bold', 'underline'),
                                            bg='white', fg='black')
                            heading.place(x=890 + 65, y=160 + 30)

                            usernameEntry = Entry(signup_window, font=('arial', 15), width=30, bd=0, bg='white',
                                                  fg='gray50')
                            usernameEntry.place(x=495 + 370 + 100, y=250 + 10)
                            usernameEntry.insert(0, 'Username')
                            usernameEntry.bind('<FocusIn>', user_enter)

                            Frame(signup_window, width=300, height=2, bg='black').place(x=495 + 370 + 100, y=267 + 20)

                            passwordEntry = Entry(signup_window, font=('arial', 15), width=30, bd=0, bg='white',
                                                  fg='gray50')
                            passwordEntry.place(x=495 + 370 + 100, y=300 + 20)
                            passwordEntry.insert(0, 'Password')
                            passwordEntry.bind('<FocusIn>', password_enter)

                            Frame(signup_window, width=300, height=2, bg='black').place(x=495 + 370 + 100, y=317 + 30)

                            hideButton = Button(signup_window, image=close_eye, bd=0, bg='white', fg='gray50'
                                                , cursor='hand2', command=hide)
                            hideButton.place(x=705 + 370 + 200, y=290 + 30)

                            confirmpasswordEntry = Entry(signup_window, font=('arial', 15), width=30, bd=0, bg='white',
                                                         fg='gray50')
                            confirmpasswordEntry.place(x=495 + 370 + 100, y=350 + 30)
                            confirmpasswordEntry.insert(0, 'confirm Password')
                            confirmpasswordEntry.bind('<FocusIn>', confirmpassword_enter)

                            Frame(signup_window, width=300, height=2, bg='black').place(x=495 + 370 + 100, y=365 + 42)

                            hideButton1 = Button(signup_window, image=close_eye, bd=0, bg='white', fg='gray50'
                                                 , cursor='hand2', command=hide1)
                            hideButton1.place(x=705 + 370 + 200, y=340 + 40)

                            signupButton = Button(signup_window, text='SIGN UP', font=(0), bd=1, bg='red', fg='white',
                                                  width=20
                                                  , cursor='hand2', command=connect_database)
                            signupButton.place(x=900 + 115, y=450)

                            signup_window.mainloop()




                        else:
                            messagebox.showerror('Error', 'The OTP was invalied pls try again:')

                    enterotp = Tk()

                    enterotp.geometry('1366x768')
                    enterotp.resizable(0, 0)
                    enterotp.title('Verify OTP')
                    bgImage = ImageTk.PhotoImage(file='Images/EMOD_BG_for_signup_page.jpg')
                    enterotp.state('zoomed')

                    bglabel = Label(enterotp, image=bgImage)
                    bglabel.place(x=0, y=0)

                    otpEntry = Entry(enterotp, width=12, bd=0, font=('', 12), bg='white', fg='gray50')
                    otpEntry.place(x=935 + 140, y=250)
                    otpEntry.insert(0, 'Enter the OTP')
                    otpEntry.bind('<FocusIn>', otp_enter)

                    Frame(enterotp, width=110, height=2, bg='black').place(x=935 + 135, y=268)

                    emailidenteredinfolable = Label(enterotp, font=('', 14),
                                                    text='Note: \nEmail ID you have entered is : \n\n' f'{emailid}',
                                                    bg='white', fg='gray50')
                    emailidenteredinfolable.place(x=870 + 140, y=300)

                    otpinfolable = Label(enterotp, font=('', 14),
                                         text='The OTP have sent to your Email.\nUse that OTP to Create an account.',
                                         bg='white', fg='gray50')
                    otpinfolable.place(x=870 + 125, y=400 + 25)

                    verifyotpButton = Button(enterotp, text='Verify OTP', font=(0), bd=1, bg='red', fg='white', width=20
                                             , cursor='hand2', command=verify_otp)
                    verifyotpButton.place(x=900 + 120, y=500 + 50)

                    gotologinbtn = Button(text='go to login', fg='blue', bd=0, font=('', 14, 'underline', 'bold'),cursor='hand2'
                                          ,command=login_page)
                    gotologinbtn.place(x=1240, y=745)

                    enterotp.mainloop()

                elif emailidEntry.get() == '':
                    messagebox.showerror('Error', 'Email ID required.')

                elif emailidcheck=='False':
                    messagebox.showerror('Error','Email ID you entered doesnot existes.')

    def login_page():
        emailverification.destroy()
        from LOGIN2 import Login
        Login()


    emailverification = Tk()
    emailverification.geometry('1366x768')
    emailverification.title('Email Verification')
    emailverification.state('zoomed')

    bgImage = ImageTk.PhotoImage(file='Images/EMOD_BG_for_signup_page.jpg')


    bglabel = Label(emailverification, image=bgImage)
    bglabel.place(x=0, y=0)

    emailidEntry = Entry(emailverification, width=40, bd=0,font=('',12), bg='white', fg='gray50')
    emailidEntry.place(x=800+150, y=250)
    emailidEntry.insert(0, 'Email ID')
    emailidEntry.bind('<FocusIn>', emailid_enter)

    Frame(emailverification, width=370, height=2, bg='black').place(x=800+150, y=270)

    emailinfolable = Label(emailverification,
                           text='NOTE: The OTP will send to the\n email id you enter.\n You will receive the OTP from emol OTP.',
                           font=('',15),bg='white', fg='gray50')
    emailinfolable.place(x=780+150, y=350)

    sendotpButton = Button(emailverification, text='Send OTP', font=(0), bd=1, bg='red', fg='white', width=20
                           ,height=2, cursor='hand2', command=send_otp)
    sendotpButton.place(x=890+130, y=540)

    loginpageButton = Button(emailverification, text='go to login', font=('Lucida Handwrit', 11, 'bold', 'underline'), bd=0,
                             bg='white', fg='blue'
                             , cursor='hand2', command=login_page)
    loginpageButton.place(x=1090+150, y=750)

    emailverification.mainloop()

