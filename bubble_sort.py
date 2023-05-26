
#bubble sort algorithm (simple)
array = [51, 42, 32, 65, 78, 90, 67, 12, 34, 58]
for i in range(0, len(array)):
    for j in range(0, len(array)-1):
        if array[j] > array[j+1]:
            temp = array[j]
            array[j] = array[j+1]
            array[j+1] = temp
print(array)

#bubble sort algorithm (complex)
def bubble_sort(arr):
    for j in range(0, len(arr)):
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
    print(arr)

arr = [21, 45, 67, 87, 98, 50, 66, 12]
result = bubble_sort(arr)
