
#question 2a: setting up the 2D array
import random

#Initialize the 2D array with all zeros
arr = [[0 for j in range(10)] for i in range(10)]

#Fill the array with random numbers between 1 and 100
for i in range(10):
    for j in range(10):
        arr[i][j] = random.randint(1, 100)

#Print the array to verify
def print_array_2(arr):
    for i in range(10):
        for j in range(10):
            print(arr[i][j], end= "|")
        print()

print_array_2(arr)
print("")
print("")

#question 2bi: bubble sort 2D array
array_length = 10
for x in range(0, array_length):
    for y in range(0, array_length -1):
        for z in range(0, array_length - 1):
            if arr[x][z] > arr[x][z+1]:
                temp = arr[x][z]
                arr[x][z] = arr[x][z+1]
                arr[x][z+1] = temp

for i in range(10):
    for j in range(10):
        print(arr[i][j], end= "|")
    print()


#question 2bii: create the procedure before / after
def print_array_1(arr):
    for i in range(10):
        for j in range(10):
            print(arr[i][j], end= "|")
        print()

print_array_1(arr)

#question 2ci: binary_search() function
def binary_search(arr, lower, upper, number):
    if upper >= lower:
        mid = (lower+(upper-1)) // 2
        if arr[0][mid] == number:
            return mid
        else:
            if arr[0][mid] > number:
                return(arr, lower, mid-1, number)
            else:
                return(arr, mid+1, upper, number )
    return -1

#question 2cii: test binary_search() twice

test_1 = int(input("Enter the first number: "))
result = binary_search(arr, 0, 11, test_1)
test_2 = int(input("Enter the second number: "))
result = binary_search(arr, 0, 11, test_2)




