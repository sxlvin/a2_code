
#Question 2ai: decalring class card, its attributes and constructor
class Card:
    def __init__(self, number, colour):
        self.__number = number #integer
        self.__colour = colour #string
    
#Question 2aii: class method GetNumber() & GetColour()

    def GetNumber(self):
        return self.__number
    
    def GetColour(self):
        return self.__colour
    
#Question 2aiii: declare the cards

one_red = (1, "red")
two_red = (2, "red")
three_red = (3, "red")
four_red = (4, "red")
five_red = (5, "red")

one_blue = (1, "blue")
two_blue = (2, "blue")
three_blue = (3, "blue")
four_blue  = (4, "blue")
five_blue = (5, "blue")

one_yellow = (1, "yellow")
two_yellow = (2, "yellow")
three_yellow = (3, "yellow")
four_yellow = (4, "yellow")
five_yellow = (5, "yellow")

#Question 2bi: declaring the class hand, its attributes and constructor

class Hand:
    def __init__(self, card_1, card_2, card_3, card_4, card_5):
        self.__cards = []                    #array
        self.__first_card = 0                #integer
        self.__number_card = 5               #integer
        self.__cards.append(card_1)
        self.__cards.append(card_2)
        self.__cards.append(card_3)
        self.__cards.append(card_4)
        self.__cards.append(card_5)

#Question 2bii: class method GetCard()

    def GetCard(self, index):
        return self.__cards[index]
    
#Question 2biii: player_1 & player_2

player_1 = Hand(one_red, two_red, three_red, four_red, one_yellow)
player_2 = Hand(two_yellow, three_yellow, four_yellow, five_yellow, one_blue)

#Question 2ci: write the calculate value function
#Question 2cii: amend program for two players

def CalculateValue(player):
    score = 0
    for i in range(5):
        card = player.GetCard(i)
        if card.GetColour() == "red":
            score = score + 5 + card.GetNumber()
        if card.GetColour() == "blue":
            score = score + 10 + card.GetNumber()
        if card.GetColour() == "yellow":
            score = score + 15 + card.GetNumber()
    return score


result_1 = CalculateValue(player_1)
result_2 = CalculateValue(player_2)

if result_1 > result_2:
    print("Player 1 wins!")
if result_2 < result_2:
    print("PLayer 2 wins!")
if result_1 == result_2:
    print("Draw!")

#Question 2ciii: test the program