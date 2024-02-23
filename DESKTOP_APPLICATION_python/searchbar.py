from tkinter import *
import re
from tkinter import END
import pymysql
from PIL import ImageTk,Image

def search_user(username):
    def showuserprofile():
        search_window.destroy()
        from showdata import showdata
        showdata(username)

    def chatting():
        search_window.destroy()
        from chatinterface import chatter
        chatter(username)

    def my_upd(search_windowidget):
        search_window = search_windowidget.widget
        index = int(search_window.curselection()[0])
        value = search_window.get(index)
        e1_str.set(value)
        l1.delete(0, END)

    def search_bar():
        search_window.destroy()
        search_user(username)

    def logout():
        search_window.destroy()
        from LOGIN2 import Login
        Login()

    def showuser():
        if e1_str.get() in my_list:
            search_window.destroy()
            from search_user import searchuser
            searchuser(e1_str.get(),username)

        else:
            from tkinter import messagebox
            messagebox.showerror('No User','No user found')


    def my_down(search_windowidget):
        l1.focus()
        l1.selection_set(0)


    search_window = Tk()
    search_window.geometry('500x500')
    bgImage = ImageTk.PhotoImage(file='Images/EMOD_BG_for_search_user_interface.jpg')
    search_window.state('zoomed')

    bglabel = Label(search_window, image=bgImage)
    bglabel.place(x=0, y=0)

    con = pymysql.connect(host='localhost',
                          user='root',
                          password=''
                          )

    mycursor = con.cursor()
    query = 'use emol'
    mycursor.execute(query)
    query = 'select username from users_data'
    mycursor.execute(query)
    usernames = mycursor.fetchall()
    my_list = [u for u, in usernames]
    font1 = ('arial', 24, 'bold')

    e1_str = StringVar()
    e1 = Entry(search_window, font=font1, textvariable=e1_str)
    e1.place(x=500, y=150)
    l1 = Listbox(search_window, height=10, font=font1, relief='flat',
                 bg='SystemButtonFace', highlightcolor='SystemButtonFace')
    l1.place(x=500, y=200)


    def get_data(*args):
        search_str = e1.get()
        l1.delete(0, END)
        for element in my_list:
            if (re.search(search_str, element, re.IGNORECASE)):
                l1.insert(END, element)


    l1.bind('<<ListboxSelect>>', my_upd)
    e1.bind('<Down>', my_down)
    l1.bind('<Right>', my_upd)
    l1.bind('<Return>', my_upd)
    e1_str.trace('w', get_data)

    searchbtn = Button(search_window, width=20, text='search', command=showuser)
    searchbtn.place(x=610, y=600)

    profile = PhotoImage(file='Images/profile_emoji.png')
    profileButton = Button(search_window, image=profile, cursor='hand2', bg='white', bd=0, command=showuserprofile)
    profileButton.place(x=150, y=695)

    search = PhotoImage(file='Images/search_emoji.png')
    searchButton = Button(search_window, image=search, cursor='hand2', bg='white', bd=0, command=search_bar)
    searchButton.place(x=500, y=695)

    chat = PhotoImage(file='Images/chat.png')
    chatButton = Button(search_window, image=chat, cursor='hand2', bg='white', bd=0, command=chatting)
    chatButton.place(x=820, y=695)

    LogoutButton = Button(search_window, text='Logout',height=2, width=15, bd=0, bg='deep sky blue', fg='white',
                          command=logout)
    LogoutButton.place(x=1200, y=700)

    search_window.mainloop()

