import random
import yaml

def listGen():
    numbers = [random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)]
    minNumber = min(numbers)
    numbers.remove(minNumber)
    numbers.append(minNumber)
    return numbers

def statGen(list):
    value = sum(list)-list[3]
    return value

def modifier(stat):
    mod = (stat-10)/2
    return int(mod//1)
    
def userGenChar():
    names = yaml.safe_load(open('names.yaml'))
    maleNames = names["male"]
    femaleNames = names["female"]

    classes = yaml.safe_load(open('classes.yaml'))

    parameters = []
    for i in range(6):
        number = listGen()
        parameters.append(statGen(number))
   
    looper = 1
    while looper:
        choice = input("Please choose the character's gender\n1. Male\n2. Female\n")
        if choice == '1':
            name = maleNames[random.randrange(len(maleNames))]
            strName = "Male"
            looper = 0
        elif choice == '2':
            name = femaleNames[random.randrange(len(maleNames))]
            strName = "Female"
            looper = 0
        else:
            print("Invalid input. Please try again.\n")
    looper = 1
    
    while looper:
        choice = input("Would you like a random class?\n1. Yes\n2. No\n")
        if choice == '1':
            randomClass = classes[random.choice(list(classes.keys()))]
            charClassStr = randomClass
            looper = 0
        if choice == '2':
            for i,j in enumerate(classes):
                print(str(i) + ". " + j)
            while looper:
                classChoice = int(input())
                if  classChoice > i:
                    print("Invalid input. Please try again. \n")
                else:
                    charClassStr = list(classes.values())[classChoice]
                    looper = 0
 
    looper = 1
    skills = charClassStr["skills"]
    #charSkills = []
    #skillChoice = [0,99]
    
    #TODO: Fix skill choice
    """while looper:
        choice = input("Would you like random skills?\n1. Yes\n2. No\n")
        if choice == '1':
            charSkills = random.sample(skills, 2)
            looper = 0
        if choice == '2':
            for i,j in enumerate(skills):
                print(str(i) + ". " + j)
            for k in range(2):
                skillChoice.append(int(input()))
                if k>0:
                    while skillChoice[0] == previousChoice:
                        skillChoice[k] = int(input("Please choose a different skill.\n"))
                        previousChoice = skillChoice[k]
                        if skillChoice[0] != previousChoice:
                            charSkills.append(skills[skillChoice[k]])
                if skillChoice[k] > i:
                    print("Invalid input. Please try again. \n")
                else:
                    charSkills.append(skills[skillChoice[k]])
                    previousChoice = skillChoice[k]
                    looper = 0"""
    
    #TODO: Add choices for parameters and items
    charSkills = random.sample(skills, 2)
    
    STR = parameters[0]
    CON = parameters[1]
    DEX = parameters[2]
    INT = parameters[3]
    WIS = parameters[4]
    CHA = parameters[5]
    HP = modifier(CON) + charClassStr["hitDice"]
    
    savingThrows = charClassStr["savingThrows"]
    
    itemChoiceOne = charClassStr["itemChoiceOne"]
    itemOne = itemChoiceOne[random.randrange(len(itemChoiceOne))]
    itemChoiceTwo = charClassStr["itemChoiceTwo"]
    itemTwo = itemChoiceTwo[random.randrange(len(itemChoiceTwo))]
    itemThree = charClassStr["itemThree"]
    feats = charClassStr["features"]
    
    print("Name: " + name)
    print("Gender: " + strName)
    print("Class: " + charClassStr["name"])
    print("HP: " + str(HP))
    print("Skills: " + charSkills[0] + " , " + charSkills[1])
    try:
        print("Saving Throws: " + savingThrows[0] + " (" + str(modifier(eval(savingThrows[0]))) + "), " + savingThrows[1] + " (" + str(modifier(eval(savingThrows[1]))) + ")")
    except Exception as e:
        print("Saving Throws: " + savingThrows[0] + ", " + savingThrows[1])
    print("STR = " + str(STR) + " (" + str(modifier(STR)) + ")")
    print("CON = " + str(CON) + " (" + str(modifier(CON)) + ")")
    print("DEX = " + str(DEX) + " (" + str(modifier(DEX)) + ")")
    print("INT = " + str(INT) + " (" + str(modifier(INT)) + ")")
    print("WIS = " + str(WIS) + " (" + str(modifier(WIS)) + ")")
    print("CHA = " + str(CHA) + " (" + str(modifier(CHA)) + ")")
    print("\033[1mInventory:\033[0m")
    print(itemOne)
    print(itemTwo)
    for i in itemThree:
        print(i)
    print("\033[1mFeatures:\033[0m")
    for i in feats:
        print(i)
