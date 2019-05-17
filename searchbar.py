#!C:/Python37/python
import mysql.connector
import cgi
conn = mysql.connector.connect(host='localhost', database='test1', user='root', password='')
c = conn.cursor()
form = cgi.FieldStorage()
ht = str(form.getvalue('sbhtp'))
cnm = str(form.getvalue('sbcnm'))
sql = "select h_name, h_type, h_code, h_city from adminaddhotel where h_type='%s' AND h_city='%s'" % (ht, cnm)
c.execute(sql)
row = c.fetchall()
print("Content-type: text/html\r\n\r\n")
print("<!DOCTYPE html>")
print("<html>")
print("<head>")
print("<link rel='stylesheet' href='style.css'>")
print("</head>")
print("<body class='rhr'>")
print("<label class='head1'>Total hotels</label>")
print("<table  border='1' class='border'>")
print("<tr><th>H_Name</th><th>H_Type</th><th>H_Code</th><th>H_City</th></tr>")
for i in row:
    print("<tr><td><a href='annapurna.html'>%s</a></td><td>%s</td><td>%s</td><td>%s</td></tr>" % (i[0], i[1], i[2], i[3]))

print("</table>")
print("</body>")
print("</html>")
conn.commit()
c.close()