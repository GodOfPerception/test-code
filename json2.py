"""Print the firm and the employees from following json
{
"employees":
[
{
"name": "Alice",
"role": "dev",
"nbr": 1
},
{
"name": "Bob",
"role": "dev",
"nbr": 2
}
],
"firm":
{
"name": "Charlie's Waffle Emporium",
"location": "CA"
}
}

#code"""
import json

j_dataii = {
"employees": [
{
"name": "Alice",
"role": "dev",
"nbr": 1
},
{
"name": "Bob",
"role": "dev",
"nbr": 2
}
],
"firm": {
"name": "Charlie's Waffle Emporium",
"location": "CA"
}
}

jj_dataii = json.dumps(j_dataii)
dataii = json.loads(jj_dataii)

print("\nSolution 2")
firm = dataii["firm"]
print(f"Firm name: {firm['name']}")
print(f"Firm location: {firm['location']}")
