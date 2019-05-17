import mysql.connector
import sys
import io
from io import StringIO
from PIL import Image
import base64
import PIL.Image

db = mysql.connector.connect(user='root', password='pratik9595', host='localhost', database='world')

#image = Image.open('C:\wamp\www\MyProj\c2.jpg')
with open("C:\wamp\www\MyProj\c2.jpg", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())

#blob_value = open('C:\wamp\www\MyProj\c2.jpg ', 'rb').read()
sql = 'INSERT INTO img111(pic) VALUES(%s)'
args = (encoded_string, )
cursor = db.cursor()
cursor.execute(sql, args)
sql1 = 'select * from img'
cursor.execute(sql)
data = cursor.fetchone()
#print type(data[1][0])
data1=base64.b64decode(data[1][0])
file_like=StringIO.StringIO(data1)
img=PIL.Image.open(file_like)
img.show()
db.close()