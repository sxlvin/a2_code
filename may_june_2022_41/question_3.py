
#question 3a: set up queue, head pointer, tail pointer
queue_array = [""]*10
top_pointer = 0                       #integer
base_pointer = 0                      #integer
queue_full = len(queue_array) - 1
item = ""
number_of_items = 0                    #integer

#question 3b: enqueue() function
def enqueue(data_to_add):
    global base_pointer, number_of_items
    if number_of_items == 10:
        return False
    queue_array[base_pointer] = data_to_add
    if base_pointer >= 9:
        base_pointer = 0
    else:
        base_pointer = base_pointer + 1
    number_of_items = number_of_items + 1
    return True

#question 3c: dequeue()
def dequeue():
    global end_pointer, item, top_pointer
    if number_of_items == 0:
        return False
    else:
        temp = queue_array[top_pointer]
        queue_array[top_pointer] = item
        top_pointer = top_pointer + 1
        return temp

#question 3di: input mechanism
#question 3dii: test your program
for i in range(0, 11):
    string = str(input("Enter a string: "))
    if i == 10:
        print("Unsuccessful")
    else:
        enqueue(string)
        print("Successful")
        print(queue_array)

print("First Value: ", dequeue())
print("Second Value: ", dequeue())
print(queue_array)
