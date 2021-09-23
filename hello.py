#!/usr/bin/env python3
import os
import json

print("Content-type:text\html\r\n\r\n")
print("<title>Test CGI</title>")
print("<p>hello world!</p>")

#print(os.environ)
json_obj = json.dumps(dict(os.environ), indent=4)
#print("json_obj: ", json_obj)

for param in os.environ.keys():
	if (param=="QUERY_STRING"):
		print("<b>%20s</b>: %s<br>" % (param, os.environ[param]))
