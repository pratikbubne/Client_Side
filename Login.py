#!C:/Python37/python
import mysql.connector
import cgi
conn = mysql.connector.connect(host='localhost', database='test1', user='root', password='')
c = conn.cursor()
form = cgi.FieldStorage()
um = str(form.getvalue('u_name'))
pd = str(form.getvalue('u_pwd'))
sql = "select mobile_no,paswd from userregister where mobile_no='%s'" % (um)
c.execute(sql)
row = c.fetchone()
print("Content-type: text/html\r\n\r\n")
if row[0] == um and row[1] == pd:
    print("<script>window.location.href = 'HomePage.html';window.alert('Welcome')</script>")
else:
    print("<script>window.location.href = 'Login.html';window.alert('User id or Password is wrong..!')</script>")
c.close()

