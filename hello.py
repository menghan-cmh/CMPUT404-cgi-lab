#!/usr/bin/env python3

import os
import json
import cgi

from templates import login_page, secret_page, after_login_incorrect
import secret

# print("Content-Type: application/json")
# print()

# Q1
# json_object = json.dumps(dict(os.environ), indent = 4)
# print(json_object)

# Q2
# for variable in os.environ.keys():
#     print(variable)
#     if (variable == "QUERY_STRING"):
#         print(os.environ.get("QUERY_STRING"))

#     # Q3
#     if (variable == "HTTP_USER_AGENT"):
#         print(os.environ.get("HTTP_USER_AGENT"))

# Q4
form = cgi.FieldStorage()
username = form.getvalue("username")
password = form.getvalue("password")

# cookies = dict(os.environ.get("HTTP_COOKIE"))
cookies = [c.strip() for c in os.environ.get("HTTP_COOKIE").split(';')]
login_cookie = "LoggedIn=true" in cookies
if login_cookie:
    print(secret_page(secret.username, secret.password))
elif not (username and password):
    print(login_page())
else:
    login_immediate = False
    if secret.username == username and secret.password == password:
        print("Set-Cookie:LoggedIn=true;", end="")
        login_immediate = True

    if login_immediate:
        print(secret_page(username, password))
    else:
        print(after_login_incorrect())



