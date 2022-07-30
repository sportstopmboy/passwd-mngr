# https://github.com/sportstopmboy/passwd-mngr


# ░██████╗██████╗░░█████╗░░█████╗░██████╗░████████╗░██████╗
# ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
# ╚█████╗░██████╔╝██║░░██║██║░░██║██████╔╝░░░██║░░░╚█████╗░
# ░╚═══██╗██╔═══╝░██║░░██║██║░░██║██╔══██╗░░░██║░░░░╚═══██╗
# ██████╔╝██║░░░░░╚█████╔╝╚█████╔╝██║░░██║░░░██║░░░██████╔╝
# ╚═════╝░╚═╝░░░░░░╚════╝░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═════╝░


# Anonymous Awareness - https://bit.ly/anonymousawareness                                                                                                                                 
# Steam - https://steamcommunity.com/id/sports_top_mboy   
# Personal Website** - https://spoorts.000webhostapp.com



import random
from tabulate import tabulate
import json
import os.path

print("\033[1;35mWelcome! \033[1;37mType \033[1;33mhelp\033[1;0m\033[1;37m for a list of available commands")

def write_json(data, filename="passlist.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

file_exists = os.path.exists('passlist.json')

if file_exists != True:
    data = {
        "passlist" : []
    }
    write_json(data)

json_passlist = json.load(open("passlist.json"))



def newpass():
    characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', '$', '%', '&', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']
    
    name = input("\033[1;37mName for Credentials:\033[1;0m ")
    username = input("\033[1;37mUserame:\033[1;0m ")
    choice  = int(input('''\033[1;37m1. Custom password
2. Randomly generated password
Choice (1 or 2):\033[1;0m '''))
    password = []

    if choice == 1:
        password = input("\033[1;32mInput custom password:\033[1;0m ")

    elif choice == 2:
        for length in range(14):
            password.append(random.choice(characters))

    table = [["\033[0;33mName", "Username", "Password"], [f"\033[1;0m{name}", username, ''.join(password)]]
    print(tabulate(table, headers='firstrow'))
    with open("passlist.json") as json_file:
        data = json.load(json_file)
        temp = data["passlist"]
        y = {name: [username, ''.join(password)]}
        temp.append(y)
    write_json(data)


def help():
    table = [["\033[1;33mCommand\033[0;0m", "\033[0;33mDescription"], ["\033[1;37mhelp\033[0;0m", "get a list of available commands"], ["\033[1;37mnewpass\033[0;0m", "create a new username, password set"], ["\033[1;37mlistpass\033[0;0m", "list credential sets created"], ["\033[1;37mview {credential set}\033[1;0m", "view username, password set"], ["\033[1;37mremove {credential set}\033[1;0m", "remove username, password set"], ["\033[1;37mexit\033[1;0m", "close the program"]]
    print(tabulate(table, headers='firstrow'))


def listpass():
    table = [["\033[0;33mName"]]
    json_passlist = json.load(open("passlist.json"))
    passlist = json_passlist.get("passlist")
    for credset in passlist:
        for item in credset:
            itemlist = []
            itemlist.append("\033[0;37m" + item)
            table.append(itemlist)
    print(tabulate(table, headers='firstrow'))
 

def view(credname):
    tries = 0
    json_passlist = json.load(open("passlist.json"))
    passlist = json_passlist.get("passlist")
    for credset in passlist:
        if credname in credset:
            userpass = credset.get(credname)
            table = [["\033[0;33mName", "Username", "Password"], [f"\033[1;0m{x[1]}", userpass[0], userpass[1]]]
            print(tabulate(table, headers='firstrow'))
        else:
            tries = tries + 1
    if tries == len(passlist):
        print("Sorry, but that item does not exist.")


def remove(credname):
    json_passlist = json.load(open("passlist.json"))
    passlist = json_passlist.get("passlist")
    found = False
    while found != True:
        for i in range(len(passlist)):
            if ''.join(list(passlist[i].keys())) == credname:
                for credset in passlist:
                    if credname in credset:
                        userpass = credset.get(credname)
                        table = [["\033[0;33mName", "Username", "Password"], [f"\033[1;0m{x[1]}", userpass[0], userpass[1]]]
                        print(tabulate(table, headers='firstrow'))
                del passlist[i]
                data = {
                "passlist" : passlist
                }
                write_json(data=data)
                found = True
                print(f"\033[1;31mRemoved {credname}\033[1;0m")
    found = False


while True:
    command = input("\033[1;32mpasswd-mngr\033[1;0m:\033[1;34m~ $\033[1;0m ")
    if command == "newpass":
        newpass()
    elif command == "help":
        help()
    elif command == "exit":
        break
    elif command == "listpass":
        listpass()
    elif "view" in command:
        x = command.split()
        if len(x) <= 1:
            print("You need to specify an item")
        else:
            view(credname=x[1])
    elif "remove" in command:
        x = command.split()
        if len(x) <= 1:
            print("You need to specify an item")
        else:
            remove(credname=x[1])
    else:
        print("Sorry, that command doesn't exist")
