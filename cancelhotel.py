#!C:/Python37/python
import mysql.connector
import cgi
conn = mysql.connector.connect(host='localhost', database='test', user='root', password='pratik9595')
c = conn.cursor()
form = cgi.FieldStorage()
onm = str(form.getvalue('o_name'))
hnm = str(form.getvalue('h_name'))
htp = str(form.getvalue('h_type'))
hct = str(form.getvalue('h_city'))
sql = "INSERT INTO hotelcancel(o_name, h_name, h_type, h_city) VALUES('%s','%s','%s','%s')" % (onm, hnm, htp, hct)
c.execute(sql)
conn.commit()
c.close()
print("Content-type: text/html\r\n\r\n")
print("<script>window.location.href = 'HotelCancel.html';window.alert('Request Send Succesfully...')</script>")