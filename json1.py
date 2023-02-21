Read the json and print out the hobbies
{
"name": "John",
"age": 50,
"is_married": false,
"profession": null,
"hobbies": ["traveling", "photography"]
}

### #code

import json
#problem 1
j_data = {
"name": "John",
"age": 50,
"is_married": False,
"profession": None,
"hobbies": ["traveling", "photography"]
}
jj_data= json.dumps(j_data)
data = json.loads(jj_data)
print("solution 1")
for hobby in data["hobbies"]:
print(hobby)
