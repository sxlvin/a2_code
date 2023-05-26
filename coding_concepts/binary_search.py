
#binary search algorithm (simple)
array = [11, 21, 31, 41, 51, 61, 71, 81, 91]
flag = True
number = int(input("Enter your number: "))
length = len(array)

mid = length // 2

if array[mid] == number:
    print("Found")

if number < array[mid]:
    while flag:
        mid = (0 + mid) // 2
        if array[mid] == number:
            print("Found")
            exit()

if number > array[mid]:
    while flag:
        mid = (((mid+1) + (len(array)-1))) // 2
        if array[mid] == number:
            print("Found")
            exit()


#binary search algorithm (complex)
def binary_search(arr, low, high, number, flag):
    if high >= low:
        mid = (high+low) // 2
    
    if arr[mid] == number:
        flag == True
        return flag
    
    if arr[mid] > number:
        return binary_search(arr, low, mid-1, number, flag)
    
    else:
        return binary_search(arr, mid+1, high, number, flag)
    
arr = [11, 21, 31, 41, 51, 61, 71, 81, 91]
number = int(input("Please enter number to be found: "))
flag = False

result = binary_search(arr, 0, len(arr), number, flag)
if result == flag:
    print("Found")
else:
    print("Not Found")
