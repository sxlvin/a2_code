
#linear search algorithm (simple)
count = 0
array = [11, 21, 31, 41, 51, 61, 71, 81, 91]
number = int(input("Please enter number you want to find: "))
for i in range(0, len(array)):
    count  = count + 1
    if array[i] == number:
        print("Found!")

if count == len(array):
    print("Not Found")


#linear search algorith (complex)
def linear_search(array, number, flag):
    for i in range(0, len(array)):
        if array[i] == number:
            flag == True
            return flag

array = [11, 21, 31, 41, 51, 61, 71, 81, 91]
number = int(input("Please enter number to be found: "))
flag = False

result = linear_search(array, number, flag)
if result == flag:
    print("Found")
else:
    print("Not Found")
