import os

##Pro Manager

##Attempts to make a directory to store projects. If directory already exists ignores.
try:
    os.mkdir('I:/ProjectManager')
except FileExistsError:
    pass

class menus:
    def projectManageMenu():
        global projectMenuInput
        print("Welcome to Pro Manager")
        print("1. Create A New Project")
        print("2. Edit an Exisitng Project")
        print("3. Exit")
        projectMenuInput = int(input("Select an Option"))

    def createProject():
        print("1. Enter a Project Deadline")
        print("2. Enter a Project Client")
        print("3. Enter a Project Price")
        print("4. Return to Main Menu")
        createProjectInput = int(input("Select an Option"))
        if createProjectInput == 1:
            menuFunctionality.projectDeadline()
        if createProjectInput == 4:
            menus.projectManageMenu()

    def editProject():
        files = os.listdir('I:/ProjectManager/')
        for number, letter in enumerate(files):
            print(number, letter)
        
class menuFunctionality:
    global currentDir
    def projectManagerFunc(projectMenuInput):
        if projectMenuInput == 1:
            projectName = input("Enter a Project Name")
            try:
                os.mkdir('I:/ProjectManager/' + projectName + '/')
                currentDir = 'I:/ProjectManager/' + projectName + '/'
                print(currentDir)
                menus.createProject()
            except FileExistsError:
                print("Project Already Exists")
        elif projectMenuInput == 2:
            menus.editProject()
        elif projectMenuInput == 3:
            exit()

    def projectDeadline():
        projectDeadlineInput = input("Enter the project deadline")
        with open(currentDir + 'Project Deadline.txt' + 'w') as f:
            f.write(projectDeadlineInput)

while True: 
    menus.projectManageMenu()
    print("")
    menuFunctionality.projectManagerFunc(projectMenuInput)

