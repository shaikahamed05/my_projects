import random
import smtplib
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql
from verify_email import verify_email

def forgetpass():
    def emailid_enter(event):
        if emailidEntry.get() == 'Email ID':
            emailidEntry.delete(0, END)
            emailidEntry.config(width=35, bd=0, bg='white', fg='black')


    def send_otp():
        emailid = str(emailidEntry.get())
        emailidcheck = str(verify_email(emailid))

        con = pymysql.connect(host='localhost',
                              user='root',
                              password=''
                              )
        mycursor = con.cursor()

        mycursor.execute('use emol')

        query = 'select * from users_data where email_id =%s'
        mycursor.execute(query, emailid)

        row = mycursor.fetchone()

        if row != None:
            emailid_1 = emailidEntry.get()
            if True:
                if emailidcheck == 'True':
                    emailid_2 = emailid_1
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login('emobotpsender@gmail.com', 'bvksbebimbmmjfbs')
                    otp = ''.join(([str(random.randint(0, 9)) for i in range(6)]))
                    OTP = str(otp)
                    SUBJECT = 'EMOL Forgot Password OTP:'
                    TEXT = OTP + ' Is Your EMOL Forgot password OTP'
                    msg = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
                    server.sendmail('emolotpsender@gmail.com', emailid, msg)
                    server.quit()
                    emailverification.destroy()

                    def otp_enter(event):
                        if otpEntry.get() == 'OTP':
                            otpEntry.delete(0, END)
                            otpEntry.config(width=35, bd=0, bg='white', fg='black')

                    def verify_otp():
                        otp1 = otpEntry.get()
                        if otp1 == OTP:
                            messagebox.showinfo('Verified', 'Your Email is Verified Seccussfuly:')
                            enterotp.destroy()
                            emailid_4 = emailid_2

                            def connect_database():
                                if passwordEntry.get() == '' or confirmpasswordEntry.get() == '':
                                    messagebox.showerror('Error', 'All Fields Are Required')
                                elif passwordEntry.get() != confirmpasswordEntry.get():
                                    messagebox.showerror('Error', 'Password mismatch Error')
                                else:

                                    try:
                                        con = pymysql.connect(host='localhost',
                                                              user='root',
                                                              password=''
                                                              )
                                        mycursor = con.cursor()
                                    except:
                                        messagebox.showerror('Error', 'Database Connectivity Issue Pls Try again')
                                        return


                                    mycursor.execute('use emol')

                                    query11 = 'select username from users_data  where email_id = %s '
                                    mycursor.execute(query11,emailid_4)
                                    rows1 = str(mycursor.fetchall())
                                    user_name11 = rows1.strip("(),'")

                                    query = 'update users_data set password = %s where username = %s'
                                    mycursor.execute(query, (passwordEntry.get(),str(user_name11)))
                                    con.commit()
                                    con.close()
                                    messagebox.showinfo('Success', 'Password is successfuly updated:')
                                    signup_window.destroy()
                                    import LOGIN


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


                            con = pymysql.connect(host='localhost',
                                                      user='root',
                                                      password=''
                                                      )
                            mycursor = con.cursor()


                            mycursor.execute('use emol')

                            query1 = 'select username from users_data  where email_id = %s '
                            mycursor.execute(query1, emailid_4)
                            rows = str(mycursor.fetchall())
                            user_name1 = rows.strip("(),'")

                            signup_window = Tk()
                            signup_window.geometry('1366x768')
                            signup_window.title('signup page')
                            signup_window.state('zoomed')
                            bgImage = ImageTk.PhotoImage(file='Images/EMOD_BG_for_login_page_1.jpg')

                            close_eye = PhotoImage(file='Images/close_eye.png')
                            open_eye = PhotoImage(file='Images/open_eyes.png')

                            bglabel = Label(signup_window, image=bgImage)
                            bglabel.place(x=0, y=0)

                            heading = Label(signup_window, text='RESET YOUR ACCOUNT PASSWORD',
                                            font=('Microsoft Yahei UI Light', 9, 'bold', 'underline'),
                                            bg='white', fg='black')
                            heading.place(x=870, y=170)

                            user_name_data = Label(signup_window, text=f'YOUR USER NAME IS: {user_name1}',
                                                   bg='white', fg='black')
                            user_name_data.place(x=870, y=220)

                            passwordEntry = Entry(signup_window, width=35, bd=0, bg='white', fg='gray50')
                            passwordEntry.place(x=850, y=260)
                            passwordEntry.insert(0, 'Password')
                            passwordEntry.bind('<FocusIn>', password_enter)

                            Frame(signup_window, width=211.5, height=2, bg='black').place(x=850, y=275)

                            hideButton = Button(signup_window, image=close_eye, bd=0, bg='white', fg='gray50'
                                                , cursor='hand2', command=hide)
                            hideButton.place(x=1070, y=255)

                            confirmpasswordEntry = Entry(signup_window, width=35, bd=0, bg='white', fg='gray50')
                            confirmpasswordEntry.place(x=850, y=320)
                            confirmpasswordEntry.insert(0, 'confirm Password')
                            confirmpasswordEntry.bind('<FocusIn>', confirmpassword_enter)

                            Frame(signup_window, width=211.5, height=2, bg='black').place(x=850, y=335)

                            hideButton1 = Button(signup_window,image=close_eye, bd=0, bg='white', fg='gray50'
                                                 , cursor='hand2', command=hide1)
                            hideButton1.place(x=1070, y=315)

                            signupButton = Button(signup_window, text='CONFORM', font=(0), bd=1, bg='red', fg='white',
                                                  width=20
                                                  , cursor='hand2', command=connect_database)
                            signupButton.place(x=890, y=400)

                            signup_window.mainloop()


                        else:
                            messagebox.showerror('Error', 'The OTP was invalied pls try again:')

                    enterotp = Tk()

                    enterotp.geometry('1366x768')
                    enterotp.title('Verify OTP')
                    enterotp.state('zoomed')
                    bgImage = ImageTk.PhotoImage(file='Images/EMOD_BG_for_login_page_1.jpg')

                    bglabel = Label(enterotp, image=bgImage)
                    bglabel.place(x=0, y=0)

                    otpEntry = Entry(enterotp, width=10, bd=0, bg='white', fg='gray50')
                    otpEntry.place(x=960, y=225)
                    otpEntry.insert(0, 'OTP')
                    otpEntry.bind('<FocusIn>', otp_enter)

                    Frame(enterotp, width=60, height=2, bg='black').place(x=950, y=240)

                    emailidenteredinfolable = Label(enterotp,
                                                    text='Note: \nEmail ID you have entered is :',
                                                    bg='white', fg='gray50')
                    emailidenteredinfolable.place(x=900, y=270)

                    emailidenteredinfolable = Label(enterotp,
                                                    text=f'{emailid}',
                                                    bg='white', fg='black')
                    emailidenteredinfolable.place(x=890, y=320)

                    otpinfolable = Label(enterotp,
                                         text='NOTE: The OTP have sent to your Email.\nUse that OTP to Create an account.',
                                         bg='white', fg='gray50')
                    otpinfolable.place(x=880, y=380)

                    verifyotpButton = Button(enterotp, text='Verify OTP', font=(0), bd=1, bg='red', fg='white', width=20
                                             , cursor='hand2', command=verify_otp)
                    verifyotpButton.place(x=890, y=460)

                    enterotp.mainloop()

                elif emailidEntry.get() == '':
                    messagebox.showerror('Error', 'Email ID required.')

                elif emailidcheck == 'False':
                    messagebox.showerror('Error', 'Email ID you entered doesnot existes.')
        else:
            messagebox.showerror('Error', 'Email ID you entered doesnot existes.')


    def login_page():
        emailverification.destroy()
        import LOGIN


    emailverification = Tk()

    emailverification.geometry('790x512')
    emailverification.state('zoomed')
    emailverification.title('Email Verification')
    bgImage = ImageTk.PhotoImage(file='Images/EMOD_BG_for_signup_page.jpg')

    bglabel = Label(emailverification, image=bgImage)
    bglabel.place(x=0, y=0)

    emailidEntry = Entry(emailverification,font=('',12), width=35, bd=0, bg='white', fg='gray50')
    emailidEntry.place(x=815+150, y=230)
    emailidEntry.insert(0, 'Email ID')
    emailidEntry.bind('<FocusIn>', emailid_enter)

    Frame(emailverification, width=350, height=2, bg='black').place(x=815+150, y=250)

    emailinfolable = Label(emailverification,font=('', 12),
                           text='NOTE: The OTP will send to the\n email id you enter.\n You will receive the OTP from emol OTP.',
                           bg='white', fg='gray50')
    emailinfolable.place(x=845+150, y=280)

    sendotpButton = Button(emailverification, text='Send OTP', font=(0), bd=1, bg='red', fg='white', width=20
                           , cursor='hand2', command=send_otp)
    sendotpButton.place(x=1020, y=400)

    loginpageButton = Button(emailverification, text='go to login', font=('Lucida Handwrit', 12, 'bold', 'underline'),
                             bd=0,
                             bg='white', fg='blue'
                             , cursor='hand2', command=login_page)
    loginpageButton.place(x=1230, y=653+100)

    emailverification.mainloop()

