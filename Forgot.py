#!C:/Python37/python
import mysql.connector
import cgi
conn = mysql.connector.connect(host='localhost', database='test1', user='root', password='')
c = conn.cursor()
form = cgi.FieldStorage()
user_name = str(form.getvalue('c_name'))
old_pass = str(form.getvalue('u_opwd'))
new_pass = str(form.getvalue('u_npwd'))
sql1 = "select mobile_no,paswd from userregister where mobile_no='%s'" % (user_name)
c.execute(sql1)
row = c.fetchone()
print("Content-type: text/html\r\n\r\n")
if row[0] == user_name and row[1] == old_pass:
    sql = "update userregister set paswd='%s' where mobile_no='%s'" % (new_pass, user_name)
    c.execute(sql)
    print("<script>window.location.href='Login.html';window.alert('You have Successfully Changed your password ')</script>")
else:
    print("<script>window.location.href='forgotpassword.html';window.alert('please enter valid user and Password')</script>")
conn.commit()
c.close()