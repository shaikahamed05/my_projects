import pymysql

con=pymysql.connect(host='localhost',user='root',password='',database='emol')
mycursor=con.cursor()

def insertpost(username):
    from PIL import Image

    def resize_image(input_path, output_path, new_width, new_height):
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
    input_path = 'static/upload_posts/posts.png'
    output_path = 'static/upload_posts/posts.png'
    new_width = 500  # Adjust the new width as needed
    new_height = 500  # Adjust the new height as needed

    resize_image(input_path, output_path, new_width, new_height)

    # updating the image
    try:
        image_path = 'static/upload_posts/posts.png'
        with open(image_path, 'rb') as file:
            image_data = file.read()

        try:

            query = f'create table {username}(id int auto_increment primary key not null,posts longblob)'
            mycursor.execute(query)
        except:
            print('table already exists')

            query = f'insert into {username} (posts) values(%s)'
            mycursor.execute(query, image_data)
            con.commit()
            con.close()


    except:
        print('image is not found')

