import random
from tabulate import tabulate
import json
import os.path
from getpass import getpass



def hashpass(password):
    passno = []
    for letter in password[::-1]:
        passno.append(ord(letter))

    algno = 0
    passnohash = []
    for item in passno:
        if algno == 0:
            passnohash.append(int(item) + 2 * 2 - 3)
            algno += 1
        elif algno == 1:
            passnohash.append(int(item) + 22)
            algno +=1
            algno += 1
        elif algno == 2:
            passnohash.append(int(item) - 34)
            algno +=1
        elif algno == 3:
            passnohash.append(int(item) * 2)
            algno +=1
        elif algno == 4:
            passnohash.append(int(item) * 2 - 13)
            algno +=1
        elif algno == 5:
            passnohash.append(int(item) - 2 * 2 + 13)
            algno +=1
        elif algno == 6:
            passnohash.append(int(item) - 31 * 2)
            algno = 0


    passfinlhash = []
    alg2no = 0
    for item in passnohash:
        if alg2no == 0:
            passfinlhash.append(chr(int(item)))
            passfinlhash.append(str(item))
            alg2no += 1
        elif alg2no == 1:
            passfinlhash.append(chr(int(item)))
            alg2no += 1
        elif alg2no == 2:
            passfinlhash.append(str(item * 3 - 69))
            passfinlhash.append(chr(int(item)))
            passfinlhash.append(str(item))
            alg2no += 1
        elif algno == 3:
            passfinlhash.append(chr(int(item)))
            alg2no = 0

    finalhash = "".join(passfinlhash)
    return finalhash





passfile_exists = os.path.exists('p4s5wd.txt')

if passfile_exists == True:
    with open("p4s5wd.txt", "r", encoding="utf-8") as passfile:
        passinfile = passfile.read()
    
    password = getpass("\033[1;36mPlease enter your password:\033[1;0m ")
    finalhash = hashpass(password)
    if str(finalhash) == str(passinfile):
        print("\033[1;35mWelcome! \033[1;37mType \033[1;33mhelp\033[1;0m\033[1;37m for a list of available commands")
    else:
        print("\033[1;31mWrong Password.\033[1;0m")
        exit()

else:
    password = input("\033[1;36mPlease create a password:\033[1;0m ")
    finalhash = hashpass(password)
    with open("p4s5wd.txt", "w", encoding="utf-8") as passfile:
        passfile.write(finalhash)
    
    with open("p4s5wd.txt", "r", encoding="utf-8") as passfile:
        passinfile = passfile.read()
    
    password = getpass("\033[1;36mPlease enter your password:\033[1;0m ")
    finalhash = hashpass(password)
    if str(finalhash) == str(passinfile):
        print("\033[1;35mWelcome! \033[1;37mType \033[1;33mhelp\033[1;0m\033[1;37m for a list of available commands")
    else:
        print("\033[1;31mWrong Password.\033[1;0m")
        exit()





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
        password = input("\033[1;37mInput custom password:\033[1;0m ")

    elif choice == 2:
        for length in range(14):
            password.append(random.choice(characters))

    else:
        print("\033[1;31mSorry, that's not a valid option\033[1;0m")

    table = [["\033[0;33mName", "Username", "Password"], [f"\033[1;0m{name}", username, ''.join(password)]]
    print(tabulate(table, headers='firstrow'))
    with open("passlist.json") as json_file:
        data = json.load(json_file)
        temp = data["passlist"]
        y = {name: [username, ''.join(password)]}
        temp.append(y)
    write_json(data)



def help():
    table = [["\033[1;33mCommand\033[0;0m", "\033[0;33mDescription"], ["\033[1;37mhelp\033[0;0m", "get a list of available commands"], ["\033[1;37mnewpass\033[0;0m", "create a new username, password set"], ["\033[1;37mlistpass\033[0;0m", "list credential sets created"], ["\033[1;37mview {credential set}\033[1;0m", "view username, password set"], ["\033[1;37mremove {credential set}\033[1;0m", "remove username, password set"], ["\033[1;37mchangepass\033[1;0m", "change password used to unlock the password manager"], ["\033[1;37mexit\033[1;0m", "close the program"]]
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
        print("\033[1;31mSorry, but that item does not exist.\033[1;0m")



def remove(credname):
    json_passlist = json.load(open("passlist.json"))
    passlist = json_passlist.get("passlist")
    tries = 0
    found = None
    while found != True:
        for i in range(len(passlist)):
            if ''.join(list(passlist[i].keys())) == credname:
                for credset in passlist:
                    if credname in credset:
                        userpass = credset.get(credname)
                        table = [["\033[0;33mName", "Username", "Password"], [f"\033[1;0m{credname}", userpass[0], userpass[1]]]
                        print(tabulate(table, headers='firstrow'))
                del passlist[i]
                data = {
                "passlist" : passlist
                }
                write_json(data=data)
                found = True
                print(f"\033[1;31mRemoved {credname}\033[1;0m") 
            else:
                tries += 1
    if tries == len(passlist) and found != True:
        print("\033[1;31mSorry, but that item does not exist.\033[1;0m")



def changepass():
    with open("p4s5wd.txt", "r", encoding="utf-8") as passfile:
        passinfile = passfile.read()
    
    password = getpass("\033[1;36mPlease enter your password:\033[1;0m ")
    finalhash = hashpass(password)
    if str(finalhash) == str(passinfile):
        newpassword = input("\033[1;36mPlease enter a new password:\033[1;0m ")
        finalhash = hashpass(newpassword)
        with open("p4s5wd.txt", "w", encoding="utf-8") as passfile:
            passfile.write(finalhash)
        print("\033[1;32mSuccessfully Changed Password.\033[1;0m")
    else:
        print("\033[1;31mWrong Password.\033[1;0m")



def editpass(credname):
    tries = 0
    json_passlist = json.load(open("passlist.json"))
    passlist = json_passlist.get("passlist")
    found = None
    while found != True and tries <= len(passlist):
        for credset in passlist:
            if credname in credset:
                choice = input('''\033[1;37mWhat would you like to edit?
1. Credential Name
2. Username
3. Password
Choice (1, 2 or 3):\033[1;0m ''')

                if int(choice) == 1:
                    userpass = credset.get(credname)
                    newcredname = input("\033[1;36mNew Name For Credentials:\033[1;0m ")
                    newset = credset
                    json_passlist = json.load(open("passlist.json"))
                    passlist = json_passlist.get("passlist")

                    with open("passlist.json", "r", encoding="utf-8") as json_file:
                        data = json.load(json_file)
                        temp = data["passlist"]
                        y = {newcredname: [userpass[0], userpass[1]]}
                        temp.append(y)
                        temp.remove(newset)

                    with open("passlist.json", "w", encoding="utf-8") as passfile:
                        data = {
                        "passlist" : temp
                        }
                        write_json(data=data)
                    print("\033[1;32mSuccessfully Updated Credentials\033[1;0m")
                    json_passlist = json.load(open("passlist.json"))
                    passlist = json_passlist.get("passlist")
                    for credset in passlist:
                        if newcredname in credset:
                            userpass = credset.get(newcredname)
                            table = [["\033[0;33mName", "Username", "Password"], [f"\033[1;0m{newcredname}", userpass[0], userpass[1]]]
                            print(tabulate(table, headers='firstrow'))
                    found = True


                elif int(choice) == 2:
                    userpass = credset.get(credname)
                    newuser = input("\033[1;36mNew Username:\033[1;0m ")
                    newset = credset
                    passlist.remove(credset)
                    newset.update({credname: [newuser, userpass[1]]})
                    passlist.append(newset)
                    with open("passlist.json", "w", encoding="utf-8") as passfile:
                        data = {
                        "passlist" : passlist
                        }
                        write_json(data=data)
                    print("\033[1;32mSuccessfully Updated Username\033[1;0m")
                    userpass = credset.get(credname)
                    table = [["\033[0;33mName", "Username", "Password"], [f"\033[1;0m{credname}", userpass[0], userpass[1]]]
                    print(tabulate(table, headers='firstrow'))
                    found = True


                elif int(choice) == 3:
                    userpass = credset.get(credname)
                    passchoice = input('''\033[1;37mDo you want to set a new custom or randomly generated password?
1. Custom
2. Randomly Generated
Choice (1 or 2):\033[1;0m ''')
                    if int(passchoice) == 1: 
                        newpass = input("\033[1;36mNew Password:\033[1;0m ")
                        newset = credset
                        passlist.remove(credset)
                        newset.update({credname: [userpass[0], newpass]})
                        passlist.append(newset)
                        with open("passlist.json", "w", encoding="utf-8") as passfile:
                            data = {
                            "passlist" : passlist
                            }
                            write_json(data=data)
                        print("\033[1;32mSuccessfully Updated Password\033[1;0m")
                        userpass = credset.get(credname)
                        table = [["\033[0;33mName", "Username", "Password"], [f"\033[1;0m{credname}", userpass[0], userpass[1]]]
                        print(tabulate(table, headers='firstrow'))
                        found = True
                    
                    if int(passchoice) == 2:
                        characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', '$', '%', '&', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']
                        randpass = []
                        for length in range(14):
                            randpass.append(random.choice(characters))
                        newpass = ''.join(randpass)
                        newset = credset
                        passlist.remove(credset)
                        newset.update({credname: [userpass[0], newpass]})
                        passlist.append(newset)
                        with open("passlist.json", "w", encoding="utf-8") as passfile:
                            data = {
                            "passlist" : passlist
                            }
                            write_json(data=data)
                        print("\033[1;32mSuccessfully Updated Password\033[1;0m")
                        userpass = credset.get(credname)
                        table = [["\033[0;33mName", "Username", "Password"], [f"\033[1;0m{credname}", userpass[0], userpass[1]]]
                        print(tabulate(table, headers='firstrow'))
                        found = True
                    found = True

                else:
                    print("\033[1;31mSorry, that's not a valid option\033[1;0m")
            
            else:
                tries = tries + 1
        if tries == len(passlist):
            print("\033[1;31mSorry, but that item does not exist.\033[1;0m")





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
            print("\033[1;31mYou need to specify an item.\033[1;0m")
        else:
            view(credname=x[1])
    elif "remove" in command:
        x = command.split()
        if len(x) <= 1:
            print("\033[1;31mYou need to specify an item.\033[1;0m")
        else:
            remove(credname=x[1])
    elif command == "changepass":
        changepass()
    elif "editpass" in command:
        x = command.split()
        if len(x) <= 1:
            print("\033[1;31mYou need to specify an item.\033[1;0m")
        else:
            editpass(credname=x[1])
    else:
        print("\033[1;31mSorry, that command doesn't exist.\033[1;0m")
