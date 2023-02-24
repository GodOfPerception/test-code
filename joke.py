"""This is the API to get random jokes, 
https://official-joke-api.appspot.com/random_joke

Your program should
Print a random joke
Ask user , do you want to see another Joke?
If user says "Y" or yes, It will call again the API and print another Joke
If User types "N" or "no" If will write a message , Thanks for your time and terminate
If user types anything else, The program should print "Could not understand you, Please type Y, Yes, N or No.

#code"""
import json
from urllib.request import urlopen
with urlopen("https://official-joke-api.appspot.com/random_joke") as u:
    data = u.read()
def jokes():
    m = json.loads(data)
    v=json.dumps(m, indent=2)
    return m["setup"],m["punchline"]

j=jokes()


def jokemech():
    print("Wanna hear a joke type Y/N")

    r = input()
    if(r=="y" or r=="Y"):
        print(j)
        jokemech()

    elif(r=="n" or r=="N"):
        print("Thanks for your time")
    else:
        print("Could not understand you, Please type Y, N")
        jokemech()
print(j)
jokemech()
