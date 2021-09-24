#!/usr/bin/env python3
import cgi
import cgitb
import secret
from templates import *
import os
import json

form = cgi.FieldStorage()

username_ch = form.getvalue('username')
password_ch = form.getvalue('password')

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - Second CGI program</title>")
print("</head>")
print("<body>")
# print("<p><b>Username</b> %s <b>password</b></p>" % (username, password))
print("</body>")
print("</html>")

for param in os.environ.keys():
    if (param == "HTTP_COOKIE"):
        print("<b>%20s</b>: here%s<br>" % (param, os.environ[param]))
        username = os.environ[param].get("username")
        password = os.environ[param].get("password")
        break

if username == username_ch and password == password_ch:
    print(secret_page(username, password))
