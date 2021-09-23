#!/usr/bin/env python3
import cgi, cigitb

form - cgi.FieldStorage()

username = form.getvalue('username')
password = form.getvalue('password')

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - Second CGI program</title>")
print("</head>")
print("<body>")
print("<p><b>Username</b> %s <b>password</b>" % (username, password))
print("</body")
print("</html>")

