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

def jokes():
    with urlopen("https://official-joke-api.appspot.com/random_joke") as u:
        data = u.read()
    m = json.loads(data)
    return m["setup"], m["punchline"]

def jokemech():
    print("Wanna hear a joke? Type Y/N")

    r = input().lower()
    if r == "y":
        print(jokes())
        jokemech()
    elif r == "n":
        print("Thanks for your time!")
    else:
        print("Could not understand you. Please type Y or N.")
        jokemech()

jokemech()
