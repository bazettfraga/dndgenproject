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

names = yaml.safe_load(open('names.yaml'))
maleNames = names["male"]
femaleNames = names["female"]

classes = yaml.safe_load(open('classes.yaml'))
randomClass = classes[random.choice(list(classes.keys()))]
skills = randomClass["skills"]
randomSkills = random.sample(skills, 2)
itemChoiceOne = randomClass["itemChoiceOne"]
itemOne = itemChoiceOne[random.randrange(len(itemChoiceOne))]
itemChoiceTwo = randomClass["itemChoiceTwo"]
itemTwo = itemChoiceTwo[random.randrange(len(itemChoiceTwo))]
itemThree = randomClass["itemThree"]
savingThrows = randomClass["savingThrows"]
feats = randomClass["features"]

#value = statGen(numbers)
#descString = f"{numbers[0]} + {numbers[1]} + {numbers[2]} = \033[1m{value}\033[0m"

parameters = []
for i in range(6):
    number = listGen()
    parameters.append(statGen(number))

STR = parameters[0]
CON = parameters[1]
DEX = parameters[2]
INT = parameters[3]
WIS = parameters[4]
CHA = parameters[5]
HP = modifier(CON) + randomClass["hitDice"]

if random.randint(0,1):
    print("Name: " + maleNames[random.randrange(len(maleNames))])
    print("Gender: Male")
else:
    print("Name: " + femaleNames[random.randrange(len(maleNames))])
    print("Gender: Female")
print("Class: " + randomClass["name"])
print("HP: " + str(HP))
print("Skills: " + randomSkills[0] + " , " + randomSkills[1])
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
