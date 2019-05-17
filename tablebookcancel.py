#!c:/python37/python
import mysql.connector
import cgi
from datetime import date
conn = mysql.connector.connect(host='localhost', database='test1', user='root', password='')
c = conn.cursor()
#cc = conn.cursor()
form = cgi.FieldStorage()
hcd = str(form.getvalue('h_code'))
cnm = str(form.getvalue('c_name'))
rsn = str(form.getvalue('reason'))
dt = str(date.today())
#sql = "upsate booktable set status = 'Booking Cancel' where cst_name = '%s' and htl_name= '%s'"%(hcd,cnm)
sql1 = "INSERT INTO tablebookcancel (h_code,c_name, reason, date) VALUES ('%s','%s','%s','%s') " % (hcd, cnm, rsn, dt)
c.execute(sql1)
#cc.execute(sql)
conn.commit()
c.close()
#cc.close()
print("Content-type: text/html\r\n\r\n")
print("<script>window.location.href = 'BookingCancle.html';</script>")
