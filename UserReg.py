#!C:/Python37/python
import mysql.connector
import cgi, cgitb
conn = mysql.connector.connect(host='localhost', database='test1', user='root', password='')
c = conn.cursor()
form = cgi.FieldStorage()
fnm = form.getvalue('fname')
lnm = form.getvalue('lname')
uml = form.getvalue('umail')
umb = form.getvalue('umob')
uad = form.getvalue('uaddrs')
pd = form.getvalue('pwd')
sql = "INSERT INTO userregister (first_name, last_name, mail, mobile_no,address, paswd) VALUES('%s','%s','%s','%s','%s','%s') " % (fnm, lnm, uml, umb, uad, pd)
c.execute(sql)
conn.commit()
c.close()
print("Content-type: text/html\r\n\r\n")
print("<script>window.location.href = 'HomePage.html';window.alert('Welcome')</script>")