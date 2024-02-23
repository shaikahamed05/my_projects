import pymysql


def insert_image_into_db(image_path):
    with open(image_path, 'rb') as file:
        image_data = file.read()

    try:
        con = pymysql.connect(host='localhost',user='root',password='',database='emol')
        mycursor = con.cursor()
        username='ahamed'

        #sql_insert = "update users_data set user_image=%s where username=%s"
        sql_insert = "INSERT INTO image (image) VALUES (%s)"

        mycursor.execute(sql_insert, (image_data))

        con.commit()

        print("Image inserted successfully!")

    except pymysql.Error as e:
        print(f"Error inserting image: {e}")

