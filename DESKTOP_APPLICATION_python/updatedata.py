from tkinter import filedialog
from tkinter import *
import tkinter as tk
from PIL import ImageTk
from tkinter import messagebox
import pymysql
from PIL import Image
from tkcalendar import *
import cv2

def updatedata(username,):
    def back_profile():
        profile_window.destroy()
        from showdata import showdata
        showdata(username)

    def phonenumber_enter(event):
        if phonenumberEntry.get() == f'{phone}':
            phonenumberEntry.delete(0, END)
            phonenumberEntry.config(width=12, bd=0, bg='light gray', fg='black')



    def upload_img():
        global get_image
        global img1

        get_image = filedialog.askopenfilename(initialdir='', title='select image file',
                                               filetype=(('JPG File', '.jpg'),
                                                         ('PNG File', '.png'),
                                                         ('All files', '.txt')))
        print(get_image)
        img = cv2.imread(get_image, cv2.IMREAD_UNCHANGED)
        dimensions = img.shape

        # height, width, number of channels in image
        height = img.shape[0]
        width = img.shape[1]
        channels = img.shape[2]

        print('Image Dimension    : ', dimensions)
        print('Image Height       : ', height)
        print('Image Width        : ', width)
        print('Number of Channels : ', channels)
        if width >= 4000:
            image_path = get_image
            image = cv2.imread(image_path)

            # Display the original and cropped images

            scale_percent = 4.5  # percent of original size
            width = int(image.shape[1] * scale_percent / 100)
            height = int(image.shape[0] * scale_percent / 100)
            dim = (width, height)

            # resize image
            resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

            print('Resized Dimensions : ', resized.shape)

            # Determine the minimum resized (width or height)
            min_dimension = min(resized.shape[0], resized.shape[1])

            # Calculate the starting points for the cropping
            start_x = (resized.shape[1] - min_dimension) // 2
            start_y = (resized.shape[0] - min_dimension) // 2

            # Perform the cropping
            cropped_image = resized[start_y:start_y + min_dimension, start_x:start_x + min_dimension]


        elif width >= 2000:
            image_path = get_image
            image = cv2.imread(image_path)

            # Display the original and cropped images

            scale_percent = 8  # percent of original size
            width = int(image.shape[1] * scale_percent / 100)
            height = int(image.shape[0] * scale_percent / 100)
            dim = (width, height)

            # resize image
            resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

            print('Resized Dimensions : ', resized.shape)

            # Determine the minimum resized (width or height)
            min_dimension = min(resized.shape[0], resized.shape[1])

            # Calculate the starting points for the cropping
            start_x = (resized.shape[1] - min_dimension) // 2
            start_y = (resized.shape[0] - min_dimension) // 2

            # Perform the cropping
            cropped_image = resized[start_y:start_y + min_dimension, start_x:start_x + min_dimension]


        else:
            image_path = get_image
            image = cv2.imread(image_path)

            # Display the original and cropped images

            scale_percent = 30  # percent of original size
            width = int(image.shape[1] * scale_percent / 100)
            height = int(image.shape[0] * scale_percent / 100)
            dim = (width, height)

            # resize image
            resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

            print('Resized Dimensions : ', resized.shape)

            # Determine the minimum resized (width or height)
            min_dimension = min(resized.shape[0], resized.shape[1])

            # Calculate the starting points for the cropping
            start_x = (resized.shape[1] - min_dimension) // 2
            start_y = (resized.shape[0] - min_dimension) // 2

            # Perform the cropping
            cropped_image = resized[start_y:start_y + min_dimension, start_x:start_x + min_dimension]


        cv2.imwrite('Images/resized.jpg', cropped_image)
        img1 = Image.open('Images/resized.jpg')
        resized_image = img1.resize((150, 150))
        photo2 = ImageTk.PhotoImage(resized_image)
        lbl.config(image=photo2)
        lbl.image = photo2



    def conver_image_into_binary(filename):
        with open(filename, 'rb') as file:
            photo_image = file.read()
        return photo_image

    def pick_date(event):
        global cal, date_window

        date_window = Toplevel()
        date_window.grab_set()
        date_window.geometry('250x220+590+370')
        cal = Calendar(date_window, selectmode='day',
                       date_pattern='mm/dd/y')
        cal.place(x=0, y=0)

        submit_btn = Button(date_window, text='submit', command=grab_date)
        submit_btn.place(x=80, y=190)


    def grab_date():
        dob_entry.delete(0, END)
        dob_entry.insert(0, cal.get_date())
        date_window.destroy()


    def insert_image():
        bio=bioEntry.get('1.0',END)
        bio1=str(bio.rsplit())
        bio1=bio1.strip("[]'")
        bio1=bio1.replace("',",'')
        bio1=bio1.replace("'",'')
        dob=dob_entry.get()
        phone=phonenumberEntry.get()

        gen=gender.get()
        con = pymysql.connect(host='localhost',
                                  user='root',
                                  password=''
                                  )
        mycursor = con.cursor()
        mycursor.execute(f'use {username}')
        image_photo = conver_image_into_binary('Images/resized.jpg')
        #query = 'insert into userdata(user_name,email,phone,gender,DOB,bio,profile_img) values(%s,%s,%s,%s,%s,%s,%s)'
        query = 'update userdata set user_name=%s,email=%s,phone=%s,gender=%s,DOB=%s,bio=%s,profile_img=%s'
        mycursor.execute(query, (username,useremailid,phone,gen,dob,bio1,image_photo))
        con.commit()
        con.close()
        messagebox.showinfo('Success', 'Registration is successful')
        profile_window.destroy()
        from showdata import showdata
        showdata(username)




    con = pymysql.connect(host='localhost',
                          user='root',
                          password='',
                          database='emol'
                          )
    # emol db
    mycursor = con.cursor()
    query = 'use emol'
    mycursor.execute(query)
    query = 'select email_id from users_data where username=%s'
    mycursor.execute(query, f'{username}')
    row = mycursor.fetchone()
    emailid = str(row)
    useremailid = emailid.strip("(),'")


    con1 = pymysql.connect(host='localhost',
                                      user='root',
                                      password=''
                                      )
    mycursor = con1.cursor()
    mycursor1 = con1.cursor()
    mycursor2 = con1.cursor()
    mycursor3 = con1.cursor()
    mycursor4 = con1.cursor()
    query = f'use {username}'
    mycursor3.execute(query)
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
    query = 'select phone from userdata'
    mycursor4.execute(query)
    row4 = mycursor4.fetchone()
    phonedb = str(row4)
    phone = phonedb.strip("(),'")
    query = 'select * from userdata'
    mycursor3.execute(query)
    row3 = mycursor3.fetchone()
    userimg = row3[7]
    with open('Images/user_profile1.jpg', 'wb') as file:
        file.write(userimg)





    global get_image
    global img

    profile_window = Tk()
    profile_window.state('zoomed')
    profile_window.geometry('1366x768')
    profile_window.title('welcomeuser page')
    profile_window.title('login page')
    bgImage = ImageTk.PhotoImage(file='Images/EMOD_BG_for_user_interface_datasaver.jpg')

    bglabel = Label(profile_window, image=bgImage)
    bglabel.place(x=0, y=0)

    usernamelabel = Label(profile_window, text=f'Hello {username}', font=('Lucida Handwrit', 12, 'bold',),
                          bg='black', fg='white')
    usernamelabel.place(x=1200, y=40)

    usernamelabel1 = Label(profile_window, text='USERNAME : ', font=('Lucida Handwrit', 7, 'bold',UNDERLINE),
                           bg='white', fg='black')
    usernamelabel1.place(x=30+200, y=90+100)

    usernameEntry1 = Label(profile_window, text=f'{username}', bd=0, bg='white', fg='black')
    usernameEntry1.place(x=30+200, y=120+100)

    biolabel = Label(profile_window, text='BIO ', font=('Lucida Handwrit', 7, 'bold',UNDERLINE), bg='white',
                     fg='black')
    biolabel.place(x=30+200, y=150+100)

    bioEntry=tk.Text(profile_window , height=8 , width=40, bg='white')
    bioEntry.place(x=30+200, y=180+100)
    bioEntry.insert(1.0, bio)



    emailidlabel = Label(profile_window, text='Email ID', font=('Lucida Handwrit', 7, 'bold',UNDERLINE),
                         bg='white', fg='black')
    emailidlabel.place(x=30+200, y=210+125+100)

    emailidEntry = Label(profile_window, text=useremailid, bd=0, bg='white', fg='black')
    emailidEntry.place(x=30+200, y=240+125+100)

    # phone number

    phonenumberlabel = Label(profile_window, text='PHONE NUMBER', font=('Lucida Handwrit', 7, 'bold',UNDERLINE),
                             bg='white', fg='black')
    phonenumberlabel.place(x=30+200, y=270+125+100)

    phonenumberEntry = Entry(profile_window, width=14, bd=0, bg='light gray', fg='black')
    phonenumberEntry.place(x=30+200, y=300+125+100)
    phonenumberEntry.insert(0, f'{phone}')
    phonenumberEntry.bind('<FocusIn>', phonenumber_enter)

    # gender

    genderlabel = Label(profile_window, text='GENDER', font=('Lucida Handwrit', 7, 'bold',UNDERLINE), bg='white',
                        fg='black')
    genderlabel.place(x=30+200, y=330+125+100)

    gender=StringVar()

    g1=Radiobutton(profile_window,text='Male',variable=gender,value='Male')
    g1.select()
    g1.place(x=230,y=580)

    g2=Radiobutton(profile_window,text='Female',variable=gender,value='Female')
    g2.deselect()
    g2.place(x=290,y=580)

    g3=Radiobutton(profile_window,text='Other',variable=gender,value='Other')
    g3.deselect()
    g3.place(x=370,y=580)

    # age

    DOBlabel = Label(profile_window, text='DATE OF BIRTH', font=('Lucida Handwrit', 7, 'bold',UNDERLINE),
                     bg='white',
                     fg='black')
    DOBlabel.place(x=30+200, y=390+125+100)

    dob_entry=Entry(profile_window,highlightthickness=0,relief=FLAT,bg='light gray',fg='black')
    dob_entry.place(x=30+200, y=420+125+100)
    dob_entry.insert(0, f'{dob}')
    dob_entry.bind('<1>', pick_date)


    img1 = Image.open('Images/user_profile1.jpg')
    resized_image = img1.resize((150, 150))
    user_photo = ImageTk.PhotoImage(resized_image)
    lbl=Label(profile_window,image=user_photo)
    lbl.place(x=700+200,y=200)




    uploadimg_Button = Button(profile_window, text='UPLOAD IMAGE',font=(' ', 0, 'bold', 'underline'), bd=0, bg='gray',
                                                                 fg='black', width=15
                                                                 , cursor='hand2',command=upload_img)
    uploadimg_Button.place(x=700+200, y=400)




    save_Button = Button(profile_window, text='SAVE DATA',font=(' ', 0, 'bold', 'underline'), bd=0, bg='LIGHT GREEN',
                                                                 fg='black', width=10
                                                                 , cursor='hand2',command=insert_image)
    save_Button.place(x=900+200, y=670)



    backButton = Button(profile_window, text='Back', width=10, bd=0, bg='gray', fg='black',
                            command=back_profile)
    backButton.place(x=100, y=100)

    profile_window.mainloop()

