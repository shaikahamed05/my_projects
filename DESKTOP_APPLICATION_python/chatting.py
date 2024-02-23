import tkinter as tk
import pymysql
from tkinter import *
from PIL import ImageTk,Image



def chatuser(sname,rname):
    def back():
        window.destroy()
        from chatinterface import chatter
        chatter(sname)

    con = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="chatting"
    )
    cursor = con.cursor()
    cursor.execute('show tables')
    tables=cursor.fetchall()
    my_list = [u for u, in tables]

    if f'{sname}_and_{rname}' in my_list:
        def send_message():
            message = entry.get()
            if message:
                messages_text.config(state=NORMAL)
                sender = user.get()
                query = f"INSERT INTO {sname}_and_{rname} (sender, message) VALUES (%s, %s)"
                cursor.execute(query, (sender, message))
                con.commit()
                entry.delete(0, tk.END)
                messages_text.delete(1.0, tk.END)
                messages_text.tag_configure('left', justify='left')
                messages_text.tag_add('left', 1.0, tk.END)
                query = f"SELECT sender, message FROM {sname}_and_{rname}"
                cursor.execute(query)
                messages = cursor.fetchall()
                for message in messages:
                    sender = message[0]
                    content = message[1]
                    if sender == rname:
                       display_text = f"   {sender}: {content}                                                                                                                                            \n"
                       messages_text.tag_configure('right', justify='right')
                       messages_text.tag_add('right', 1.0, tk.END)
                       messages_text.insert(tk.END, display_text)
                    else:
                       display_text = f"   {content} :{sender}     \n\n"
                       messages_text.insert(tk.END, display_text)
                messages_text.config(state=DISABLED)

        def display_messages():
            messages_text.config(state=NORMAL)
            messages_text.delete(1.0, tk.END)
            messages_text.tag_configure('left', justify='left')
            messages_text.tag_add('left', 1.0, tk.END)
            query = f"SELECT sender, message FROM {sname}_and_{rname}"
            cursor.execute(query)
            messages = cursor.fetchall()
            for message in messages:
                sender = message[0]
                content = message[1]
                if sender == rname:
                   display_text = f"   {sender}: {content}                                                                                                                                            \n"
                   messages_text.tag_configure('right',justify='right')
                   messages_text.tag_add('right',1.0,tk.END)
                   messages_text.insert(tk.END, display_text)
                else:
                   display_text = f"   {content} :{sender}     \n\n"
                   messages_text.insert(tk.END, display_text)
            messages_text.config(state=DISABLED)


    elif f'{rname}_and_{sname}' in my_list:
        def send_message():
            message = entry.get()
            if message:
                messages_text.config(state=NORMAL)
                sender = user.get()
                query = f"INSERT INTO {rname}_and_{sname} (sender, message) VALUES (%s, %s)"
                cursor.execute(query, (sender, message))
                con.commit()
                entry.delete(0, tk.END)
                messages_text.delete(1.0, tk.END)
                messages_text.tag_configure('left', justify='left')
                messages_text.tag_add('left', 1.0, tk.END)
                query = f"SELECT sender, message FROM {rname}_and_{sname}"
                cursor.execute(query)
                messages = cursor.fetchall()
                for message in messages:
                   sender = message[0]
                   content = message[1]
                   if sender == rname:
                      display_text = f"   {sender}: {content}                                                                                                                                            \n"
                      messages_text.tag_configure('right', justify='right')
                      messages_text.tag_add('right', 1.0, tk.END)
                      messages_text.insert(tk.END, display_text)
                   else:
                      display_text = f"   {content} :{sender}     \n\n"
                      messages_text.insert(tk.END, display_text)
                messages_text.config(state=DISABLED)

        def display_messages():
            messages_text.config(state=NORMAL)
            messages_text.delete(1.0, tk.END)
            query = f"SELECT sender, message FROM {rname}_and_{sname}"
            cursor.execute(query)
            messages = cursor.fetchall()
            for message in messages:
               sender = message[0]
               content = message[1]
               if sender == rname:
                  display_text = f"   {sender}: {content}                                                                                                                                            \n"
                  messages_text.tag_configure('right', justify='right')
                  messages_text.tag_add('right', 1.0, tk.END)
                  messages_text.insert(tk.END, display_text)
               else:
                  display_text = f"   {content} :{sender}     \n\n"
                  messages_text.insert(tk.END, display_text)
            messages_text.config(state=DISABLED)


    else:
        cursor.execute(f"CREATE TABLE {sname}_and_{rname} (id INT AUTO_INCREMENT PRIMARY KEY, sender VARCHAR(255), message TEXT)")

        def send_message():
            message = entry.get()
            if message:
                messages_text.config(state=NORMAL)
                sender = user.get()
                query = f"INSERT INTO {sname}_and_{rname} (sender, message) VALUES (%s, %s)"
                cursor.execute(query, (sender, message))
                con.commit()
                entry.delete(0, tk.END)
                messages_text.delete(1.0, tk.END)
                messages_text.tag_configure('left', justify='left')
                messages_text.tag_add('left', 1.0, tk.END)
                query = f"SELECT sender, message FROM {sname}_and_{rname}"
                cursor.execute(query)
                messages = cursor.fetchall()
                for message in messages:
                   sender = message[0]
                   content = message[1]
                   if sender == rname:
                      display_text = f"   {sender}: {content}                                                                                                                                            \n"
                      messages_text.tag_configure('right', justify='right')
                      messages_text.tag_add('right', 1.0, tk.END)
                      messages_text.insert(tk.END, display_text)
                   else:
                      display_text = f"   {content} :{sender}     \n\n"
                      messages_text.insert(tk.END, display_text)
                messages_text.config(state=DISABLED)



        def display_messages():
            messages_text.config(state=NORMAL)
            messages_text.delete(1.0, tk.END)
            query = f"SELECT sender, message FROM {sname}_and_{rname}"
            cursor.execute(query)
            messages = cursor.fetchall()
            for message in messages:
               sender = message[0]
               content = message[1]
               if sender == rname:
                  display_text = f"   {sender}: {content}                                                                                                                                            \n"
                  messages_text.tag_configure('right', justify='right')
                  messages_text.tag_add('right', 1.0, tk.END)
                  messages_text.insert(tk.END, display_text)
               else:
                  display_text = f"   {content} :{sender}     \n\n"
                  messages_text.insert(tk.END, display_text)
            messages_text.config(state=DISABLED)

    con2 = pymysql.connect(host='localhost',
                          user='root',
                          password=''
                          )
    cursor_4 = con2.cursor()
    query = f'use {rname}'
    cursor_4.execute(query)


    global bio
    global gender
    global dob

    con1 = pymysql.connect(host='localhost',
                          user='root',
                          password=''
                          )

    my_cursor = con1.cursor()
    my_cursor1 = con1.cursor()
    my_cursor2 = con1.cursor()
    my_cursor3 = con1.cursor()
    query = f'use {rname}'
    my_cursor.execute(query)
    query = 'select bio from userdata'
    my_cursor.execute(query)
    roww = my_cursor.fetchone()
    dbbio = str(roww)
    bio = dbbio.strip("(),'")
    query = 'select gender from userdata'
    my_cursor1.execute(query)
    row1 = my_cursor1.fetchone()
    dbgender = str(row1)
    gender = dbgender.strip("(),'")
    query = 'select dob from userdata'
    my_cursor2.execute(query)
    row2 = my_cursor2.fetchone()
    dbdob = str(row2)
    dob = dbdob.strip("(),'")
    query = 'select * from userdata'
    my_cursor3.execute(query)
    row3 = my_cursor3.fetchone()
    row3 = row3[7]
    with open('Images/user_profile.jpg', 'wb') as file:
            file.write(row3)


    window = tk.Tk()
    window.state('zoomed')


    img = Image.open('Images/user_profile.jpg')
    resized_image = img.resize((100, 100))
    user_photo = ImageTk.PhotoImage(resized_image)
    profilephoto = Label(window, image=user_photo)
    profilephoto.pack()

    # username

    usernameEntry1 = Label(window,font=('',15,'underline'), text=f'{rname} :', bd=0, bg='white', fg='black')
    usernameEntry1.place(x=550,y=20)
    # usernameEntry1.insert(0,username)

    messages_text = tk.Text(window,height=36.5,width=150,state=DISABLED)
    messages_text.pack()

    entry = tk.Entry(window,width=100)
    entry.place(x=80,y=700)

    user = tk.StringVar()
    user.set(f"{sname}")

    send_button = tk.Button(window, text="Send", command=send_message)
    send_button.place(x=700,y=700)

    back_btn = tk.Button(window, text="back", command=back)
    back_btn.place(x=20,y=20)

    display_messages()

    window.mainloop()

    con.close()


