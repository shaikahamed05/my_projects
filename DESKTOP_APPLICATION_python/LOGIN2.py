from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql


def Login():
    def login_user():

        if usernameEntry.get() == '' or passwordEntry.get() == '':
            messagebox.showerror('Error', 'All Fields Are Required')
        else:
            username = usernameEntry.get()
            password = passwordEntry.get()
            try:
                con = pymysql.connect(host='localhost',
                                      user='root',
                                      password='')
                mycursor = con.cursor()
            except:
                messagebox.showerror('Error', 'connection is not extablished try again later')
                return
            queue = 'use emol'
            mycursor.execute(queue)
            queue = 'select * from users_data where username=%s and password=%s'
            mycursor.execute(queue, (usernameEntry.get(), passwordEntry.get()))
            row = mycursor.fetchone()
            if row == None:
                messagebox.showerror('Error', 'Invalid username or password')
            else:
                messagebox.showinfo('LOGIN SUCCESSFULL', ('welcome', usernameEntry.get()))
                login_window.destroy()

                # home page program
                from showdata import showdata
                showdata(username)

    def user_enter(event):
        if usernameEntry.get() == 'Username':
            usernameEntry.delete(0, END)
            usernameEntry.config(width=35, bd=0, bg='#18C6E8', fg='black')

    def password_enter(event):
        if passwordEntry.get() == 'Password':
            passwordEntry.delete(0, END)
            passwordEntry.config(width=35, bd=0, bg='#12C5EE', fg='black')

    def forgetpass_page():
        login_window.destroy()
        from Forgetpass import forgetpass
        forgetpass()

    def signup_page():
        login_window.destroy()
        from SIGNUP import signup
        signup()

    def hide():
        hideButton.config(image=close_eye, bd=0, bg='#12C5EE', fg='black', cursor='hand2')
        passwordEntry.config(show='*')
        hideButton.config(command=show)

    def show():
        hideButton.config(image=open_eye, bd=0, bg='#12C5EE', fg='black', cursor='hand2')
        passwordEntry.config(show='')
        hideButton.config(command=hide)

    login_window = Tk()
    login_window.title('login page')
    login_window.geometry('1366x768')
    bgImage = ImageTk.PhotoImage(file='Images/updated-one.jpg')
    login_window.state('zoomed')

    close_eye = PhotoImage(file='Images/close_eye.png')
    open_eye = PhotoImage(file='Images/open_eyes.png')
    forget_emoji = PhotoImage(file='Images/forget_emoji.png')

    bglabel = Label(login_window, image=bgImage)
    bglabel.place(x=0, y=0)

    usernameEntry = Entry(login_window, width=50, bd=0, bg='#18C6E8', fg='gray50')
    usernameEntry.place(x=490 + 90, y=260 + 35)
    usernameEntry.insert(0, 'Username')
    usernameEntry.bind('<FocusIn>', user_enter)

    Frame(login_window, width=302, height=2, bg='black').place(x=490 + 90, y=275 + 35)

    passwordEntry = Entry(login_window, width=50, bd=0, bg='#12C5EE', fg='gray50')
    passwordEntry.place(x=490 + 90, y=310 + 35)
    passwordEntry.config(show='*')
    passwordEntry.insert(0, 'Password')
    passwordEntry.bind('<FocusIn>', password_enter)

    Frame(login_window, width=300, height=2, bg='black').place(x=490 + 90, y=325 + 35)

    hideButton = Button(login_window, activebackground='#12C5EE', image=close_eye, bd=0, bg='#12C5EE', fg='black'
                        , cursor='hand2', command=show)
    hideButton.place(x=790 + 90, y=300 + 35)

    forgetpasswordButton1 = Button(login_window, image=forget_emoji,
                                   bd=0, bg='#07C2F7',
                                   fg='white', activebackground='#07C2F7'
                                   , cursor='hand2', command=forgetpass_page)
    forgetpasswordButton1.place(x=800, y=360 + 35)

    forgetpasswordButton = Button(login_window, font=('Monem', 10, 'bold', 'underline'), text='Forget Password?',
                                  bd=0, bg='#07C2F7',
                                  fg='white', activebackground='#07C2F7'
                                  , cursor='hand2', command=forgetpass_page)
    forgetpasswordButton.place(x=680, y=363 + 35)

    loginButton = Button(login_window, text='LOGIN👆', font=(0), bd=1, bg='red', fg='white',
                         width=20
                         , height=2, cursor='hand2', command=login_user)
    loginButton.place(x=555 + 90, y=440 + 35)

    Frame(login_window, width=400, height=2, bg='black').place(x=446 + 90, y=540 + 35)

    createaccountButton = Button(login_window, text='CREATE  ACCOUNT',
                                 font=(' ', 0, 'bold', 'underline'), bd=0, bg='orange',
                                 fg='white', width=25
                                 , height=2, cursor='hand2', command=signup_page)
    createaccountButton.place(x=500 + 90, y=580 + 50)

    login_window.mainloop()
