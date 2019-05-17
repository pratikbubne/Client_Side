#!c:/python37/python
import mysql.connector
import cgi
conn = mysql.connector.connect(host='localhost', database='test1', user='root', password='')
c = conn.cursor()
form = cgi.FieldStorage()
onm = str(form.getvalue('o_name'))
omb = str(form.getvalue('o_mobile'))
oml = str(form.getvalue('o_mail'))
hnm = str(form.getvalue('h_name'))
hty = str(form.getvalue('h_type'))
hads = str(form.getvalue('h_address'))
hcty = str(form.getvalue('h_city'))
sql = "INSERT INTO hotelregister (onr_name, onr_mobile, onr_mail, htl_name, htl_type, htl_addrs, htl_city) VALUES ('%s','%s','%s','%s','%s','%s','%s') " % (onm, omb, oml, hnm, hty, hads, hcty)
c.execute(sql)
conn.commit()
c.close()
print("Content-type: text/html\r\n\r\n")
print("<script>window.location.href = 'hotelreg.html';</script>")
