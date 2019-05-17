#!C:/Python37/python
import mysql.connector
import cgi
from datetime import date
conn = mysql.connector.connect(host='localhost', database='test1', user='root', password='')
c = conn.cursor()
form = cgi.FieldStorage()
hc = str(form.getvalue('h_code'))
cn = str(form.getvalue('c_name'))
password = str(form.getvalue('pass'))
date = str(date.today())
sql1 = "select cst_name from booktable where email='%s'"% (cn)
c.execute(sql1)
row = c.fetchone()
print("Content-type: text/html\r\n\r\n")
if row[0] == cn:
    sql = "delete from bankregistration where username='%s' and activate_date='%s'"% (cn,date)
    c.execute(sql)
    print("<script>window.location.href='CancelBooking.html';window.alert('You have Successfully canceled your BookBank Registration ')</script>")
else:
    print("<script>window.location.href='cancelBooking.html';window.alert('please enter valid user and Password')</script>")
conn.commit()
c.close()
conn.close()