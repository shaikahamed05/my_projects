from tkinter import *
from PIL import ImageTk

def hide():
    pass

def hide1():
    pass

def connect_database():
    pass


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
heading.place(x=890+65, y=160+30)

usernameEntry = Entry(signup_window, font=('arial', 15), width=30, bd=0, bg='white', fg='gray50')
usernameEntry.place(x=495 + 370+100, y=250 + 10)
usernameEntry.insert(0, 'Username')
usernameEntry.bind('<FocusIn>', user_enter)

Frame(signup_window, width=300, height=2, bg='black').place(x=495 + 370+100, y=267 + 20)

passwordEntry = Entry(signup_window, font=('arial', 15), width=30, bd=0, bg='white', fg='gray50')
passwordEntry.place(x=495 + 370+100, y=300 + 20)
passwordEntry.insert(0, 'Password')
passwordEntry.bind('<FocusIn>', password_enter)

Frame(signup_window, width=300, height=2, bg='black').place(x=495 + 370+100, y=317 + 30)

hideButton = Button(signup_window, image=close_eye, bd=0, bg='white', fg='gray50'
                    , cursor='hand2', command=hide)
hideButton.place(x=705 + 370+200, y=290 + 30)

confirmpasswordEntry = Entry(signup_window, font=('arial', 15), width=30, bd=0, bg='white',
                             fg='gray50')
confirmpasswordEntry.place(x=495 + 370+100, y=350 + 30)
confirmpasswordEntry.insert(0, 'confirm Password')
confirmpasswordEntry.bind('<FocusIn>', confirmpassword_enter)

Frame(signup_window, width=300, height=2, bg='black').place(x=495 + 370+100, y=365 + 42)

hideButton1 = Button(signup_window, image=close_eye, bd=0, bg='white', fg='gray50'
                     , cursor='hand2', command=hide1)
hideButton1.place(x=705 + 370+200, y=340 + 40)

signupButton = Button(signup_window, text='SIGN UP', font=(0), bd=1, bg='red', fg='white',
                      width=20
                      , cursor='hand2', command=connect_database)
signupButton.place(x=900+115, y=450)

signup_window.mainloop()

