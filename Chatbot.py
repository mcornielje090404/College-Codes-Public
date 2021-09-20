## This program is a chatbot with multiple responses to each input given.

import random

## This is a function designed to allow responses to phrases regardless of punctuation at the end of the phrase ex. how are you and how are you? would be responded the same
def loopCheck(userInput,responseTable):
    for tableItem in responseTable:
        if userInput.startswith(tableItem):
            return True
    return False

## This is a function to allow a user of the program to input a question or phrase
def getInput():
    userInput = input(">>> ")
    userInput = userInput.lower()

## This is an if and else block of code that recieves inputs and turns them into responses on a random algorithim
    if loopCheck(userInput , ["hi","hello","sup", "hey", "whats up", "what's up"]):
        responseTable = ["Hi!","Hello!"]
        print(responseTable[random.randint(0,len(responseTable)-1)])
    elif loopCheck(userInput , ["bye","goodbye","see you later", "talk to you later", "see you"]):
        responseTable2 = ["See you!", "Talk later!", "Goodbye!"]
        print(responseTable2[random.randint(0,len(responseTable2)-1)])
    elif loopCheck(userInput , ["how are you", "how goes it", "how are you doing", "how has your day been", "how is your day going"]):
        responseTable3 = ["Good!", "Bad :(", "Okay!", "Just alright."]
        print(responseTable3[random.randint(0,len(responseTable3)-1)])
        print("How about you?")
    elif loopCheck(userInput , ["where are you from", "where do you come from", "what country are you from", "who created you"]):
        responseTable4 = ["I am from Moritz's computer!", "I am from M2103890 device!"]
        print(responseTable4[random.randint(0, len(responseTable4)-1)])
    elif loopCheck(userInput , ["bad", "i am sad", "not good", ":(", "very bad", "really sad" "sad", "i am really sad", "i am struggling", "struggling"]):
        responseTable5 = ["I am sorry to hear that :(", "That's not good. You should do some self care!", "I really hope it gets better soon!"]
        print(responseTable5[random.randint.(0,len(responseTable5)-1)])
    elif loopCheck(userInput , ["good", "very good", "i am doing good", "well", "i am doing well", "i am doing very good", "i am doing very well", "it is going good", "it is going well"]:
         responseTable6 = ["That's good to hear!", "I am glad to hear that.", "Brilliant!", "I hope life continues on the up!"]
         print(responseTable6[random.randint(0, len(responseTable6)-1)])
    else:
        print("I dont know what you said")

## A code that prevent instant closing of the program
while True:
    getInput()
