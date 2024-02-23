from tkinter import *
from PIL import ImageTk
import pymysql
from PIL import Image
from updatedata import updatedata
from tkinter import messagebox



def showdata(username):
    def showuser():
        mailprofile_window.destroy()
        showdata(username)


    def edit_profile():
        mailprofile_window.destroy()
        updatedata(username)

    def logout():
        mailprofile_window.destroy()
        from LOGIN2 import Login
        Login()

    def search_bar():
        mailprofile_window.destroy()
        from searchbar import search_user
        search_user(username)

    def chatting():
        mailprofile_window.destroy()
        from chatinterface import chatter
        chatter(username)



    con = pymysql.connect(host='localhost',
                          user='root',
                          password=''
                          )
    cursor4 = con.cursor()
    mycursor=con.cursor()
    try:
        query = f'use {username}'
        cursor4.execute(query)
        con.commit()
        con.close()

        global bio
        global gender
        global dob

        con = pymysql.connect(host='localhost',
                              user='root',
                              password=''
                              )

        mycursor = con.cursor()
        mycursor1 = con.cursor()
        mycursor2 = con.cursor()
        mycursor3 = con.cursor()
        try:
            query1 = f'create database {username}'
            mycursor.execute(query1)
            query1 = f'use {username}'
            mycursor.execute(query1)
            query1 = 'create table userdata (id int auto_increment primary key not null,user_name varchar(20),email varchar(100),bio varchar(150),phone varchar(10),gender varchar(6),DOB varchar(10),profile_img BLOB(52428800))'
            mycursor.execute(query1)
            with open('Images/profile.png', 'rb') as file:
                photo_imagedb = file.read()
            query = 'insert into userdata (profile_img) values(%s)'
            mycursor.execute(query, (photo_imagedb))
            con.commit()
            con.close()
        except:
            query = f'use {username}'
            mycursor.execute(query)
            query = 'select bio from userdata'
            mycursor.execute(query)
            roww = mycursor.fetchone()
            dbbio = str(roww)
            bio = dbbio.strip("(),'")
            query = 'select gender from userdata'
            mycursor1.execute(query)
            row1 = mycursor1.fetchone()
            dbgender = str(row1)
            gender = dbgender.strip("(),'")
            query = 'select dob from userdata'
            mycursor2.execute(query)
            row2 = mycursor2.fetchone()
            dbdob = str(row2)
            dob = dbdob.strip("(),'")
            query = 'select * from userdata'
            mycursor3.execute(query)
            row3 = mycursor3.fetchone()
            row3 = row3[7]
            with open('Images/user_profile.jpg', 'wb') as file:
                file.write(row3)

        mailprofile_window = Tk()
        mailprofile_window.state('zoomed')
        mailprofile_window.geometry('1366x768')
        mailprofile_window.title('welcomeuser page')
        bgImage = ImageTk.PhotoImage(file='Images/EMOD_BG_for_user_interface.jpg')

        bglabel = Label(mailprofile_window, image=bgImage)
        bglabel.place(x=0, y=0)


        profile = PhotoImage(file='Images/profile_emoji.png')
        profileButton = Button(mailprofile_window, image=profile, cursor='hand2', bg='white', bd=0,command=showuser)
        profileButton.place(x=150, y=795)
        
        # search bar navigator

        search = PhotoImage(file='Images/search_emoji.png')
        searchButton = Button(mailprofile_window, image=search, cursor='hand2', bg='white', bd=0,command=search_bar)
        searchButton.place(x=540, y=795)

        chat = PhotoImage(file='Images/chat.png')
        chatButton = Button(mailprofile_window, image=chat, cursor='hand2', bg='white', bd=0,command=chatting)
        chatButton.place(x=930, y=795)

        LogoutButton = Button(mailprofile_window, text='Logout', height=2, width=15, bd=0, bg='deep sky blue',
                              fg='white',
                              command=logout)
        LogoutButton.place(x=1300, y=800)

        usernamelabel = Label(mailprofile_window, text=f'Hello {username}',
                                  font=('Lucida Handwrit', 12, 'bold',),
                                  bg='black', fg='white')
        usernamelabel.place(x=1400, y=40)

        img = Image.open('Images/user_profile.jpg')
        resized_image = img.resize((150, 150))
        user_photo = ImageTk.PhotoImage(resized_image)
        profilephoto = Label(mailprofile_window, image=user_photo)
        profilephoto.place(x=200, y=130)

        # username

        usernameEntry1 = Label(mailprofile_window, text=username, bd=0, bg='white', fg='black')
        usernameEntry1.place(x=200, y=290)
        # usernameEntry1.insert(0,username)

        # bio

        biolabel = Label(mailprofile_window, text='BIO:', font=('Lucida Handwrit', 9, 'bold',), bg='white',
                             fg='black')
        biolabel.place(x=500, y=90+40)

        bioEntry = Label(mailprofile_window, text=bio, width=50, height=10, bd=0, bg='gray90', fg='black')
        bioEntry.place(x=500, y=115+40)

        genderlabel = Label(mailprofile_window, text='GENDER:', font=('Lucida Handwrit', 9, 'bold',),
                                bg='white',
                                fg='black')
        genderlabel.place(x=1000, y=200+40)

        genderEntry = Label(mailprofile_window, text=gender, width=10, bd=0, bg='gray90', fg='black')
        genderEntry.place(x=1000, y=225+40)

            # DOB

        DOBlabel = Label(mailprofile_window, text='DATE OF BIRTH:', font=('Lucida Handwrit', 9, 'bold',),
                             bg='white',
                             fg='black')
        DOBlabel.place(x=1000, y=170)


        DOBEntry = Label(mailprofile_window, text=dob, width=20, bd=0, bg='gray90', fg='black')
        DOBEntry.place(x=1000, y=195)

        # edit data

        editButton = Button(mailprofile_window, text='Edit Profile', width=30, bd=0, bg='gray', fg='black',
                                command=edit_profile)
        editButton.place(x=1200, y=300)


        Frame(mailprofile_window, width=10000, height=2, bg='gray').place(x=0, y=340)

        mailprofile_window.mainloop()

    except:

        global biotext
        global gendertext
        global dobtext

        try:
            biotext='No Bio Entered'
            gendertext='No gender Extered'
            dobtext='No Date of birth Entered'
            query1 = f'create database {username}'
            mycursor.execute(query1)
            query1 = f'use {username}'
            mycursor.execute(query1)
            query1 = 'create table userdata (id int auto_increment primary key not null,user_name varchar(20),email varchar(100),bio varchar(150),phone varchar(10),gender varchar(6),DOB varchar(10),profile_img BLOB(52428800))'
            mycursor.execute(query1)
            with open('Images/profile.png', 'rb') as file:
                photo_imagedb = file.read()
            query = 'insert into userdata (bio,gender,DOB,profile_img) values(%s,%s,%s,%s)'
            mycursor.execute(query, (biotext,gendertext,dobtext,photo_imagedb))
            con.commit()
            con.close()

        except:

            messagebox.showerror('Error', 'connection Lost.....\nTry Later')


        mailprofile_window = Tk()
        mailprofile_window.state('zoomed')
        mailprofile_window.geometry('1366x768')
        mailprofile_window.title('welcomeuser page1')
        bgImage = ImageTk.PhotoImage(file='Images/EMOD_BG_for_user_interface.jpg')

        bglabel = Label(mailprofile_window, image=bgImage)
        bglabel.place(x=0, y=0)


        profile = PhotoImage(file='Images/profile_emoji.png')
        profileButton = Button(mailprofile_window, image=profile, cursor='hand2', bg='white', bd=0,command=showuser)
        profileButton.place(x=150, y=795)

        search = PhotoImage(file='Images/search_emoji.png')
        searchButton = Button(mailprofile_window, image=search, cursor='hand2', bg='white', bd=0,command=search_bar)
        searchButton.place(x=540, y=795)

        chat = PhotoImage(file='Images/chat.png')
        chatButton = Button(mailprofile_window, image=chat, cursor='hand2', bg='white', bd=0,command=chatting)
        chatButton.place(x=930, y=795)

        LogoutButton = Button(mailprofile_window, text='Logout',height=2, width=15, bd=0, bg='deep sky blue', fg='white',
                            command=logout)
        LogoutButton.place(x=1300, y=800)

        usernamelabel = Label(mailprofile_window, text=f'Hello {username}',
                              font=('Lucida Handwrit', 12, 'bold',),
                              bg='black', fg='white')
        usernamelabel.place(x=1400, y=40)

        img = Image.open('Images/profile.png')
        resized_image = img.resize((150, 150))
        user_photo = ImageTk.PhotoImage(resized_image)
        profilephoto = Label(mailprofile_window, image=user_photo)
        profilephoto.place(x=200, y=130)

        # username

        usernameEntry1 = Label(mailprofile_window, text=username, bd=0, bg='white', fg='black')
        usernameEntry1.place(x=200, y=290)
        # usernameEntry1.insert(0,username)

        # bio

        biolabel = Label(mailprofile_window, text='BIO:', font=('Lucida Handwrit', 9, 'bold',), bg='white',
                         fg='black')
        biolabel.place(x=500, y=90+40)

        bioEntry = Label(mailprofile_window, text=biotext, width=50, height=5, bd=0, bg='gray90', fg='black')
        bioEntry.place(x=500, y=115+40)

        genderlabel = Label(mailprofile_window, text='GENDER:', font=('Lucida Handwrit', 9, 'bold',),
                            bg='white',
                            fg='black')
        genderlabel.place(x=1000, y=200+40)

        genderEntry = Label(mailprofile_window, text=gendertext, width=10, bd=0, bg='gray90', fg='black')
        genderEntry.place(x=1000, y=225+40)

        # DOB

        DOBlabel = Label(mailprofile_window, text='DATE OF BIRTH:', font=('Lucida Handwrit', 9, 'bold',),
                         bg='white',
                         fg='black')
        DOBlabel.place(x=1000, y=170)

        DOBEntry = Label(mailprofile_window, text=dobtext, width=20, bd=0, bg='gray90', fg='black')
        DOBEntry.place(x=1000, y=195)

        # edit data

        editButton = Button(mailprofile_window, text='Edit Profile', width=30, bd=0, bg='gray', fg='black',
                            command=edit_profile)
        editButton.place(x=1200, y=300)


        Frame(mailprofile_window, width=10000, height=2, bg='gray').place(x=0, y=340)

        mailprofile_window.mainloop()


