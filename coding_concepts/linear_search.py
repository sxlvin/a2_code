#simple code for linear search
list = [11, 12, 13, 14, 15, 16, 17, 18, 19]
number = int(input("Please enter a number: "))
flag = False
for i in range(0, len(list)-1):
    if list[i] == number:
        flag = True

if flag == True:
    print("Number found!")
else:
    print("Number not found!")

#complex code for linear search
def linear_search(x, y, z):
    for i in range(0, len(x)):
        if x[i] ==  number:
            z = True
    
    if z == True:
        print("Number Found!")
    else:
        print("Number not Found!")

arr = [11, 12, 13, 14, 15, 16, 17, 18, 19]
number = int(input("Please enter a number: "))
flag = False
linear_search(arr, number, flag)
