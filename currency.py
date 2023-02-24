"""consume this API https://api.coindesk.com/v1/bpi/currentprice.json and provide me the price of all currencies. The outcome should look like this
Currency Name -XYZ,  Rate - XYZ, Symbol - XYZ,  Updated- XYZ, UpdatedISO-XYZ, UpdatedUK-XYZ 
XYZ should be replaced by actual values. (Please understand that the time is common for all currencies)

#code"""

import json
from urllib.request import urlopen
with urlopen("https://api.coindesk.com/v1/bpi/currentprice.json") as u:
    data = u.read()
m = json.loads(data)
v=json.dumps(m, indent=2)
for i,time in zip(m["bpi"],m["time"]):
    print(f'Currency name: {m["bpi"][i]["description"]}, rate: {m["bpi"][i]["rate"]}, symbol: {m["bpi"][i]["symbol"]}, updated: {m["time"]["updated"]}, updatediso: {m["time"]["updatedISO"]}, updateduk: {m["time"]["updateduk"]} ')

