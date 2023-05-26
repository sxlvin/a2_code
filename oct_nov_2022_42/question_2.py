
#question 2a: declare class character
class Character:
    def __init__(self, name, x_coordinate, y_coordinate):
        self.__name = name
        self.__x_coordinate = x_coordinate
        self.__y_coordinate = y_coordinate

#question 2b: three get methods
    def GetName(self):
        return self.__name
    
    def GetXCoordinate(self):
        return self.__x_coordinate
    
    def GetYCoordinate(self):
        return self.__y_coordinate

#question 2c: change position method

    def ChangePosition(self, XChange, YChange):
        self.__x_coordinate += XChange
        self.__y_coordinate += YChange

#Question 2d: 1D array

character_array = []
try:
    file = open("Characters.txt", "r")
    name = file.readline().strip()
    while name != "":
        x = file.readline().strip()
        y = file.readline().strip()
        newCharacter = Character(name, int(x), int(y))
        character_array.append(newCharacter)
        name = file.readline().strip()

except IOError:
    print("File Not Found")

#Question 2e: linear_search
index = 0
flag = False
while flag!= True:
    character_input = input("Enter the character: ").lower()
    for i in range(0, len(character_array)):
        if character_input == character_array[i].GetName().lower():
            flag = True
            index = i


#Question 2f: WASD controls
letter = str(input("Enter your control letter: "))
flag = False
while flag != True:
    if letter == "W":
        character_array[index].ChangePosition(0, 1)
        flag = True
    if letter == "A":
        character_array[index].ChangePosition(-1, 0)
        flag = True
    if letter == "S":
        character_array[index].ChangePosition(0, -1)
        flag = True
    if letter == "D":
        character_array[index].ChangePosition(1, 0)
        flag = True

#Question 2gi: change position
if flag == True:
    print(f"{character_array[index].GetName()} has changed coordinate to X = {character_array[index].GetXCoordinate()} and Y = {character_array[index].GetYCoordinate()}")

#Question 2gii: test your program