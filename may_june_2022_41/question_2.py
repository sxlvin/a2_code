
#Question 2a: class balloon and constructor
class Balloon:
    def __init__(self, colour, defence_item):
        self.__health = 100
        self.__colour = colour
        self.__defence_item = defence_item
    
#Question 2b: write method for GetDefence()
    def GetDefenceItem(self):
        return self.__defence_item
    
#Question 2c: write method for ChangeHealth()
    def ChangeHealth(self, change):
        self.__health += change

#Question 2d: check whether any health is remaining
    def CheckHealth(self):
        if self.__health < 0:
            return True
        else:
            return False

#Question 2e: taking in inputs
defence = input("Enter defence item: ")
colour = input("Enter a colour: ")
Balloon_1 = Balloon(defence, colour)

#Question 2f: defend() function

def Defence(Balloon_1):
    strength = int(input("Enter strength value: "))
    Balloon_1.ChangeHealth(-strength)
    print("Defence Item: ", Balloon_1.GetDefenceItem())
    result = Balloon_1.CheckHealth()
    if result == True:
        print("No health reminaing")
    else:
        print("Health remaining")
    
    return Balloon

#Question 2gi: call the defence() function
#Question 2gii: test the code

Defence(Balloon_1)


