#!C:/Python37/python
import mysql.connector
import cgi
from datetime import date
conn = mysql.connector.connect(host='localhost', database='test1', user='root', password='')
c = conn.cursor()
form = cgi.FieldStorage()
tpl = str(form.getvalue('ttl_ppl'))
tim = str(form.getvalue('time'))
dt = str(date.today())
hcd = str(form.getvalue('h_code'))
cnm = str(form.getvalue('c_name'))
cmb = str(form.getvalue('c_mobile'))
pmt = str(form.getvalue('payment'))
sql = "INSERT INTO booktable(total_people, bk_time, bk_date, htl_code, cst_name, mobile, pay) VALUES('%s','%s','%s','%s','%s','%s','%s')" % (tpl, tim, dt, hcd, cnm, cmb, pmt)
c.execute(sql)
conn.commit()
c.close()
print("Content-type: text/html\r\n\r\n")
print("<script>window.location.href = 'Last.html';window.alert('Booking Succesfully...')</script>")