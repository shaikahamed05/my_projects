import os

import pymysql
from PIL import Image
import io

con = pymysql.connect(host='localhost',user='root',password='',database='emol')
mycursor = con.cursor()

mycursor.execute("SELECT id, image FROM image")
images = mycursor.fetchall()

con.close()

#delete the images in the static/posts path to insert new images
path='./static/posts/'
for name in os.listdir(path):
    file=path+name
    if os.path.isfile(file):
        os.remove(file)

#save images as per the id in database in static/posts path
for image_id, image_data in images:
    image = Image.open(io.BytesIO(image_data))

    filename = f'./static/posts/image_{image_id}.png'
    image.save(filename, format='PNG')

    print(f'image_{image_id}.png saved')

images_count=len(images)
print(images_count," images saved to PNG files.")
