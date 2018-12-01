import os
import random

def New_Glossary():
    MyList = []
    while True:
        word = input("Write a word to add or FIN to finish creating your glossary: ")
        if word == "FIN":
            break
        else:
            MyList.append(word)

    MyList_str="\n".join(MyList)

    #Wrighting the list into the glossary

    gloss_name = input("Choose a name for your list: ")
    path = os.path.join(r".\Lists",gloss_name)
    Gloss = open(path, "w")
    Gloss.write(MyList_str)
    Gloss.close()

def Dice(gloss_name):

    #opening the choosed glossary

    path = os.path.join(r".\Lists",gloss_name)
    Gloss = open(path,"r")
    data = Gloss.readlines()

    #Dice

    while True:
        print(data[random.randint(0,len(data)-1)])
        check = input("Press ENTER to continue, print EXIT to stop: ")
        if check == "EXIT":
            break

    Gloss.close()

path = ".\Lists"
print("You now have these glossaries to choose from:\n", os.listdir(path))
name = input("\nPrint the name of the glossary you wish to choose or NEW if you wish to create the new one: ")

if name == "NEW":
    New_Glossary()
else:
    Dice(name)








