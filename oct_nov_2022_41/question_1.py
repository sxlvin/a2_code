
#Question 1a: declare array
data_array = [""]*100

#Question 1b: read and store numbers
def readfile():
    try:
        file = open("IntegerData.txt", "r")
        for i in range(0, 100):
            line_1 = int(file.readline().strip())
            data_array[i] = line_1
        
        file.close()

    except IOError:
        print("File not found")

#Question 1c: linear searching
def findvalues():
    count = 0
    flag = True
    while flag == True:
        number = int(input("Please enter a number: "))
        if number >= 1 and number <= 100:
            flag = False
            for i in range(0, len(data_array)):
                if data_array[i] == number:
                    count = count + 1

    return count

#Question 1di: call the procedures
#Question 1dii: test the program
readfile()
print(data_array)
print("Your number is repeated " , findvalues(), " times!")

#Question 1e: bubble sort
def bubble_sort(data_array):
    for j in range(0, len(data_array)):
        for i in range(0, len(data_array)-1):
            if data_array[i] > data_array[i+1]:
                temp = data_array[i]
                data_array[i] = data_array[i+1]
                data_array[i+1] = temp
    
    print(data_array)


bubble_sort(data_array)
