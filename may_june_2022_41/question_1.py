
#question 1a: declaring the array
player_array = [None]*11
score_array = [None]*11

#question 1b: read the data in file
def read_score():
    try:
        file = open("HighScore.txt", "r")
        for i in range(0, 10):
            line_1 = file.readline().strip()
            player_array[i] = line_1
            line_2 = int(file.readline().strip())
            score_array[i] = line_2
    
    except IOError:
        print("File not found")

#question 1c: output player and score
def output_high_scores():
    for i in range(0, 11):
        print(player_array[i], score_array[i])

#Question 1di: call the functions
#Question 1dii: test the program
read_score()
output_high_scores()

#Question 1ei: new inputs and sorting
letter_1 = str(input("Please enter a letter: ")).upper()
letter_2 = str(input("Please enter a letter: ")).upper()
letter_3 = str(input("Please enter a letter: ")).upper()
letter = (letter_1 + letter_2 + letter_3)

i = 0
while i == 0:
    number = int(input("Please enter a number: "))
    if number >= 1 and number <= 100000:
        print("Valid!")
        i += 1

print(player_array)
print(score_array)


#Question 1eii: create procedure to sort
def insert_and_sort(a, b):
    player_array[len(player_array) - 1] = a
    score_array[len(player_array) - 1] = b
    
    for i in range(0, len(score_array)):
        for j in range(0, len(score_array)-1):
            if score_array[j] < score_array[j+1]:
                temp_1 = score_array[j]
                temp_2 = player_array[j]
                score_array[j] = score_array[j+1]
                player_array[j] = player_array[j+1]
                score_array[j+1] = temp_1
                player_array[j+1] = temp_2

    print(player_array)
    print(score_array)

#Question 1eiii: call procedure
insert_and_sort(letter, number)

#Question 1eiv: test the program
#Question 1f: new text file
def write_to_file():
    file_object = open("NewHighScore.txt", "w")
    for i in range(0, 10):
        file_object.write(str(player_array[i]) + "\n")
        file_object.write(str(score_array[i]) + "\n")

write_to_file()
