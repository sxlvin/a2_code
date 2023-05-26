
#insertion sort (simple)
arr = [31, 45, 65, 43, 23, 12, 21, 45, 89, 76]
for i in range(1, len(arr)):
    value = arr[i]

    while arr[i-1] > value and i > 0:
        temp = arr[i]
        arr[i] = arr[i-1]
        arr[i-1] = temp
        i = i - 1
print(arr)

#insertion sort (complex)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        value = arr[i]
    
        while arr[i-1] > value and i > 0:
            temp = arr[i]
            arr[i] = arr[i-1]
            arr[i-1] = temp
            i = i - 1
    
    print(arr)

arr = [31, 45, 65, 43, 23, 12, 21, 45, 89, 76]
result = insertion_sort(arr)

