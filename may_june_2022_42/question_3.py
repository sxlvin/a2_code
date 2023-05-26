
#Question 3a: class Card and constructor
class Card:
    def __init__(self, number, color):
        self.__number = number  #integer
        self.__color = color    #string

#Question 3b: GetNumber() & GetColor()
    def GetNumber(self):
        return self.__number
    
    def GetColor(self):
        return self.__color

#Question 3c: create array
card_array = []*30
try:
    file = open("CardValues.txt")
    name = file.readline().strip()
    while name != "":
        number = file.readline().strip()
        colour = file.readline().strip()
        new_card = Card(number, colour)
        card_array.append(new_card)
        name = file.readline().strip()
    file.close()

except IOError:
    print("File Not Found")

#Question 3d: ChooseCard()
def ChooseCard():
    flag = False
    chosen_array = []
    integer = int(input("Select a number betweeen 1 to 30: ")) - 1
    while flag != True:
        if integer < 0 or integer > 29:
            print("Invalid Number")
        for i in range(0, len(chosen_array)):
            if chosen_array[i] == integer:
                print("Card already selected!")
        if integer >= 0 or integer <= 29:
            flag = True
            chosen_array.append(integer)
    return integer

#Question 3ei: selecting 4 cards
player_1 = []
card = ChooseCard()
player_1.append(card_array[card])
for i in range(0, 29):
    print(player_1[i].GetNumber())
    print(player_1[i].GetColor())

