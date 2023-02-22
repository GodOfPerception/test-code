"""Call this API in python
https://gorest.co.in/public/v2/users
And print the details of the users.

#code"""

import json
from urllib.request import urlopen
with urlopen ("https://gorest.co.in/public/v2/users") as u:
    data=u.read().decode()

dataa = json.loads(data)

for user in dataa:
    print(user["name"])
