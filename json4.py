"""Call this API in python
https://gorest.co.in/public/v2/users
print
Number of active users
Number of inactive users
id, name and email id of Active users.

#code"""
import json
from urllib.request import urlopen
with urlopen ("https://gorest.co.in/public/v2/users") as u:
    data=u.read().decode()

dataa = json.loads(data)
active_count = 0
inactive_count = 0
for i in dataa:
    if i["status"]=="active":
        active_count = active_count + 1
    else:
        inactive_count=inactive_count+1

print(f"Number of active users: {active_count}")
print(f"Number of inactive user: {inactive_count}")
print("Data of active users")
for ii in dataa:
    if ii["status"]=="active":
        print(f'id: {ii["id"]},\n name: {ii["name"]},\n email: {ii["email"]}')
