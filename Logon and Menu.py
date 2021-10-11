
usernamearray = ["Admin"]
passwordarray = ["Password"]

def additem():
    print("1. Add to Usernames")
    print("2. Add to Passwords")
    arrayinput = input("Enter A Option")
    if arrayinput == "1":
        usernamearrayinput = input("Enter Username to Add")
        usernamearray.append(usernamearrayinput)
    elif arrayinput == "2":
        passwordarrayinput = input("Enter Password to Add")
        passwordarray.append(passwordarrayinput)
    else:
        print("Not an Option")

def removeItem():
    print("1. Remove from Username")
    print("2. Remove from Passwords")
    removeitem = input("Enter an Option")
    if removeitem == "1":
        removeitemtrue = input("Enter an item you would like to remove")
        for i in range(0, len(usernamearray)):
            if (usernamearray[i] == removeitemtrue):
                usernamearray.remove(removeitemtrue)
    elif removeitem == "2":
        removeitemtrue = input("Enter an item you would like to remove")
        for i in range(0, len(passwordarray)):
            if (passwordarray[i] == removeitemtrue):
                passwordarray.remove(removeitemtrue)
    else:
        print("Not an Option")

def viewItem():
    print("1. View Usernames")
    print("2. View Passwords")
    viewarrayinput = input("Enter an Option")
    if viewarrayinput == "1":
        print(usernamearray)
    elif viewarrayinput == "2":
        print(passwordarray)
    else:
        print("Not an Option")

def logon():
    username = input("Username:")
    password = input("Password:")
    
    for j in range(0, len(usernamearray)):
        if username == username[j]:
            password = ("Password:")
        for x in range(0, len(passwordarray)):
            if password == passwordarray[x]:
                    while True:
                        print("")
                        print("Menu:")
                        print("")
                        print("1. Add Item")
                        print("2. Remove Item")
                        print("3. View All Items")
                        print("0. Exit")
                        print("")
                        userinput = input("Enter an Option")

                        if userinput == "1":
                            additem()
                        elif userinput == "2":
                            removeItem()
                        elif userinput == "3":
                            viewItem()
                        elif userinput == "0":
                            logon()
                        else:
                                print("Not an Option")
            elif password != passwordarray[x]:
                print("Invalid Password")
                logon()
            elif username != username[j]:
                print("Username")
                logon()

logon()

