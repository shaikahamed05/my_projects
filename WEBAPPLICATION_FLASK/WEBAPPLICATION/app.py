import random
import smtplib
import os
import io
from PIL import Image
import base64
from flask import Flask, render_template, request, session, flash, url_for, redirect
import pymysql



app = Flask(__name__)
app.secret_key = 'emol'


con = pymysql.connect(host='localhost', user='root', password='', database='emol')
mycursor = con.cursor()


# Rest of your code...

@app.route("/")
def root():
    global sessionusername
    global sessionnickname
    if session.get('logged_in') == True:
        sessionusername=session['uname']
        sessionnickname=session['nickname']


        queue = "select user_image from users_data where username=%s"
        mycursor.execute(queue, sessionusername)
        

        image_data = mycursor.fetchone()[0]

        file = './static/profile_images/profileimage.png'
        if os.path.isfile(file):
            os.remove(file)
        else:
            pass

        # Convert the binary data back to an image
        image = Image.open(io.BytesIO(image_data))
        filename = './static/profile_images/profileimage.png'
        image.save(filename, format='PNG')

        try:
                directory_path = 'static/posts'
                # List all files in the directory
                files = os.listdir(directory_path)

                # Filter only files with specific extensions (e.g., '.png')
                image_files = [file for file in files if
                               file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

                # Count the number of image files
                image_count = len(image_files)

                print(f"Number of images in '{directory_path}': {image_count}")


        except Exception as e:
                print(f"Error counting images: {e}")
                image_count=0

        # Example usage

        return render_template("main.html",username=sessionusername,nickname=sessionnickname,image_count=image_count)
    return render_template("index.html")


@app.route("/Signup")
def Signup():
    return render_template("Signup.html")

@app.route("/Login")
def Login():
    return render_template("index.html")

@app.route("/Logout")
def Logout():
    session['logged_in'] = False
    session['uname'] = None
    return render_template("index.html")

@app.route("/logindb",methods=['POST'])
def loginuser():
    username=request.form['username']
    password=request.form['password']
    queue = "select * from users_data where username=%s and password=%s"
    mycursor.execute(queue, (username, password))
    

    row = mycursor.fetchone()
    if row == None:
        return render_template("index.html",errormsg='uname_password')
    else:
        query='select nickname from users_data where username=%s'
        mycursor.execute(query,username)
        

        nkname=mycursor.fetchone()
        
        global nickname
        for r in nkname:
            nickname=r
        session['logged_in'] = True
        session['uname'] = username
        session['nickname'] = nickname

        queue="select user_image from users_data where username=%s"
        mycursor.execute(queue,username)
        

        image_data = mycursor.fetchone()[0]

        file='./static/profile_images/profileimage.png'
        if os.path.isfile(file):
            os.remove(file)
        else:
            pass

        # Convert the binary data back to an image
        image = Image.open(io.BytesIO(image_data))
        filename = './static/profile_images/profileimage.png'
        image.save(filename, format='PNG')

        #count images in posts folder
        try:
            directory_path = 'static/posts'
            # List all files in the directory
            files = os.listdir(directory_path)

            # Filter only files with specific extensions (e.g., '.png')
            image_files = [file for file in files if
                           file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

            # Count the number of image files
            image_count = len(image_files)

            print(f"Number of images in '{directory_path}': {image_count}")


        except Exception as e:
            print(f"Error counting images: {e}")
            image_count=0
        
        return render_template("main.html",username=username,nickname=nickname,image_count=image_count)

@app.route("/profile",methods=['GET'])
def profile():
    username=request.args['username']
    queue='select nickname,bio from users_data where username=%s'
    mycursor.execute(queue,username)
    

    nicknamebio=mycursor.fetchall()

    
    for n,b in nicknamebio:
        nickname=n
        bio=b


    from insertpost import insertpost
    insertpost(str(username))

    #get posts from db
    try:

        # delete the images in the static/posts path to insert new images
        path = './static/posts/'
        for name in os.listdir(path):
            file = path + name
            if os.path.isfile(file):
                os.remove(file)

        mycursor.execute(f"SELECT id, posts FROM {username}")
        

        images = mycursor.fetchall()


        # save images as per the id in database in static/posts path
        for image_id, image_data in images:
            image = Image.open(io.BytesIO(image_data))

            filename = f'./static/posts/image_{image_id}.png'
            image.save(filename, format='PNG')

            print(f'image_{image_id}.png saved')

        images_count = int(len(images))

        return render_template("profile.html",username=username,nickname=nickname,bio=bio,count=images_count)
    except:
        return render_template('profile.html',username=username,nickname=nickname,bio=bio,count=0)


@app.route('/edit_profile',methods=['GET'])
def edit_profile():
    username=request.args['username']

    queue='select nickname from users_data where username=%s'
    mycursor.execute(queue,username)
    

    nickname=mycursor.fetchone()
    queue='select email_id from users_data where username=%s'
    mycursor.execute(queue,username)
    

    emailid=mycursor.fetchone()
    queue='select bio from users_data where username=%s'
    mycursor.execute(queue,username)
    

    bio=mycursor.fetchone()
    for n in nickname:
        nickname=n
    for e in emailid:
        emailid=e
    for b in bio:
        bio=b
    return render_template('edit_profile1.html',username=username,emailid=emailid,nickname=nickname,bio=bio)


@app.route("/crop_image")
def crop_image():
    return render_template('crop_image.html')


@app.route("/edit_profile_image",methods=['GET'])
def edit_profile_image():
    username=request.args['username']

    queue='select nickname from users_data where username=%s'
    mycursor.execute(queue,username)
    

    nickname=mycursor.fetchone()
    queue='select email_id from users_data where username=%s'
    mycursor.execute(queue,username)
    

    emailid=mycursor.fetchone()
    queue='select bio from users_data where username=%s'
    mycursor.execute(queue,username)
    

    bio=mycursor.fetchone()
    for n in nickname:
        nickname=n
    for e in emailid:
        emailid=e
    for b in bio:
        bio=b
    return render_template('edit_profile1.html',username=username,emailid=emailid,nickname=nickname,bio=bio)


@app.route('/saveimage', methods=['POST'])
def saveimage():
    data = request.get_json()
    dataURL = data['dataURL'].split(',')[1]  # Extract base64 data
    image_data = base64.b64decode(dataURL)

    # Save the image on the server
    filename = 'static/profile_images/profileimage.png'
    with open(filename, 'wb') as f:
        f.write(image_data)

    return render_template('edit_profile1.html')


@app.route('/postsave')
def postsave():
    return render_template('savepostes.html')


@app.route('/savepostdb', methods=['POST'])
def savepostdb():
    username = session['uname']
    data = request.get_json()
    dataURL = data['dataURL'].split(',')[1]  # Extract base64 data
    image_data = base64.b64decode(dataURL)

    # Save the image on the server
    filename = 'static/upload_posts/posts.png'
    with open(filename, 'wb') as f:
        f.write(image_data)

    # Print the username




    from insertpost import insertpost
    insertpost(username)

    from fetchpost import fetchpost
    fetchpost(username)


    images_count=fetchpost(username)
    print(images_count)


    query=f'select nickname from users_data where username={username}'
    mycursor.execute(query)
    

    nickname = mycursor.fetchone()
    for n in nickname:
        nickname = n

    query=f'select bio from users_data where username={username}'
    mycursor.execute(query)
    

    bio = mycursor.fetchone()
    for b in bio:
        bio = b


    return render_template("profile.html", username=username, nickname=nickname, bio=bio, count=images_count)



        # Return a success message
        # get posts from db





@app.route('/save', methods=['POST'])
def save():
    # Get the image and username from the form data

    username = request.form['username']
    nickname = request.form['nickname']
    bio = request.form['bio']


    # Print the username

    def reduce_image_size(input_path, output_path, new_width, new_height):
            try:
                # Open the image file
                with Image.open(input_path) as img:
                    # Resize the image
                    resized_img = img.resize((new_width, new_height))

                    # Save the resized image
                    resized_img.save(output_path)

                    print("Image resized and saved successfully!")

            except Exception as e:
                print(f"Error resizing image: {e}")

        # Example usage

    input_path = 'static/profile_images/profileimage.png'
    output_path = 'static/profile_images/profileimage.png'
    new_width = 500  # Adjust the new width as needed
    new_height = 500  # Adjust the new height as needed

    reduce_image_size(input_path, output_path, new_width, new_height)


    #updating the image
    image_path='static/profile_images/profileimage.png'
    with open(image_path, 'rb') as file:
            image_data = file.read()



    sql_insert = "update users_data set user_image=%s,nickname=%s,bio=%s where username=%s"
    #sql_insert = "INSERT INTO users_data (image) VALUES (%s)"

    mycursor.execute(sql_insert, (image_data,nickname,bio,username))
    

    con.commit()

    try:
        mycursor.execute(f"SELECT id, posts FROM {username}")
        

        images = mycursor.fetchall()

        

        # delete the images in the static/posts path to insert new images
        path = './static/posts/'
        for name in os.listdir(path):
            file = path + name
            if os.path.isfile(file):
                        os.remove(file)

        # save images as per the id in database in static/posts path
        for image_id, image_data in images:
            image = Image.open(io.BytesIO(image_data))

            filename = f'./static/posts/image_{image_id}.png'
            image.save(filename, format='PNG')

            print(f'image_{image_id}.png saved')



        images_count = int(len(images))

        return render_template("profile.html", username=username, nickname=nickname, bio=bio, count=images_count)

    except:
        return render_template('profile.html',username=username,nickname=nickname,bio=bio,count=0)




    # Return a success message
    # get posts from db




@app.route("/homepg",methods=['GET'])
def homepg():
        username=request.args['username']

        queue='select nickname from users_data where username=%s'
        mycursor.execute(queue,username)
        

        nkname=mycursor.fetchone()
        

        global nickname
        for r in nkname:
            nickname=r
        session['logged_in'] = True
        session['uname'] = username
        session['nickname'] = nickname

        #count images in posts folder
        try:
            directory_path = 'static/posts'
            # List all files in the directory
            files = os.listdir(directory_path)

            # Filter only files with specific extensions (e.g., '.png')
            image_files = [file for file in files if
                           file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

            # Count the number of image files
            image_count = len(image_files)

            print(f"Number of images in '{directory_path}': {image_count}")


        except Exception as e:
            print(f"Error counting images: {e}")
            image_count=0

        return render_template("main.html",username=username,nickname=nickname,image_count=image_count)








@app.route("/otpsend",methods=['POST'])
def otpsend():
    try:
        query = 'create database emol'
        mycursor.execute(query)

        mycursor.execute(query)
        query = 'create table users_data(id int auto_increment primary key not null,email_id varchar(100),username varchar(100), password varchar(30))'
        mycursor.execute(query)
        

    except:
        pass

    global emailid
    emailid=request.form['emailid']
    emailid=str(emailid)
    query = 'select * from users_data where email_id =%s'
    mycursor.execute(query, emailid)
    

    row = mycursor.fetchone()
    if row != None:
        return render_template("Signup.html",errormsg="user_exist")
    else:
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login('emolotpsender@gmail.com', 'zhib gztg slqw kvwq')
            otp = ''.join(([str(random.randint(0, 9)) for i in range(6)]))
            global OTP
            OTP = str(otp)
            SUBJECT = 'emol OTP to Verify:'
            TEXT = OTP + ' Is Your emol Verification Code'
            msg = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
            server.sendmail('emolotpsender@gmail.com', emailid, msg)
            server.quit()
            return render_template("OTP_Entry.html",otp=OTP,emailid=emailid)
        except:
            return render_template("Signup.html",errormsg='Invalid')

@app.route("/create",methods=['POST'])
def create():
    global username
    useremailid=emailid
    nickname=request.form['nickname']
    username=request.form['username']
    password=request.form['password']

    query = 'select * from users_data where username=%s'
    mycursor.execute(query, (username))
    

    row = mycursor.fetchone()
    if row != None:
        return render_template("registor.html",errormsg='username_exists',emailid=useremailid)
    else:
        def insert_image_into_db(image_path):
            with open(image_path, 'rb') as file:
                image_data = file.read()
            try:
                query = 'insert into users_data(email_id,nickname,username,password,user_image) values(%s,%s,%s,%s,%s)'
                mycursor.execute(query, (useremailid, nickname, username, password,image_data))
                

            except pymysql.Error as e:
                print(f"Error inserting image: {e}")
        image_path = "static/img/userprofile.png"
        insert_image_into_db(image_path)

        con.commit()

        #count images in posts folder
        try:
            directory_path = 'static/posts'
            # List all files in the directory
            files = os.listdir(directory_path)

            # Filter only files with specific extensions (e.g., '.png')
            image_files = [file for file in files if
                           file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

            # Count the number of image files
            image_count = len(image_files)

            print(f"Number of images in '{directory_path}': {image_count}")


        except Exception as e:
            print(f"Error counting images: {e}")
            image_count=0
        
        return render_template("main.html",username=username,nickname=nickname,image_count=image_count)


@app.route("/forget_otpsend",methods=['POST'])
def forget_otpsend():
    try:
        query = 'create database emol'
        mycursor.execute(query)

        mycursor.execute(query)
        query = 'create table users_data(id int auto_increment primary key not null,email_id varchar(100),username varchar(100), password varchar(30))'
        mycursor.execute(query)
        

    except:
        pass


    global emailid
    emailid=request.form['emailid']
    emailid=str(emailid)
    query = 'select * from users_data where email_id =%s'
    mycursor.execute(query, emailid)
    

    row = mycursor.fetchone()
    if row != None:
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login('emolotpsender@gmail.com', 'zhib gztg slqw kvwq')
            otp = ''.join(([str(random.randint(0, 9)) for i in range(6)]))
            global OTP
            OTP = str(otp)
            SUBJECT = 'Forget Password OTP:'
            TEXT = OTP + ' Is Your emol forget password otp'
            msg = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
            server.sendmail('emolotpsender@gmail.com', emailid, msg)
            server.quit()
            return render_template("forget_OTP_Entry.html",otp=OTP,emailid=emailid)
        except:
            return render_template("Signup.html",errormsg='Invalid')
    else:
        return render_template("Signup.html",errormsg="user_exist")


@app.route('/forgetpassword')
def forgetpassword():
    return render_template('forgetpassword.html')


@app.route("/verify_otp",methods=['POST'])
def verify_otp():
    userotp = request.form['entered_otp']
    sentotp=OTP
    useremailid=emailid
    if userotp==sentotp:
        return render_template("registor.html",emailid=useremailid)
    else:
        return render_template("OTP_Entry.html",errormsg='Invalid_OTP')

@app.route("/forget_verify_otp",methods=['POST'])
def forget_verify_otp():
    userotp = request.form['entered_otp']
    sentotp=OTP
    useremailid=emailid

    queue='select username from users_data where email_id=%s'
    mycursor.execute(queue,useremailid)
    

    uname=mycursor.fetchone()
    for r in uname:
        uname=r
    if userotp==sentotp:
        return render_template("change_password.html",emailid=useremailid,username=uname)
    else:
        return render_template("forget_OTP_Entry.html",errormsg='Invalid_OTP')

@app.route('/update_password',methods=['POST'])
def update_password():
    password=request.form['password']

    queue='update users_data set password=%s'
    mycursor.execute(queue,password)
    con.commit()
    

    return render_template('index.html')


app.run(debug=True)
#app.run(host='192.168.1.4',debug=True)