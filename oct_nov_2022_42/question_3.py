
#question 3a: set up queue code, top and base pointer
queue = [""]*100
top_pointer = 0
base_pointer = 0
queuefull = len(queue) - 1
item = ""

#question 3b: enqueue() function
def enqueue(item):
    global top_pointer
    if top_pointer > queuefull:
        print("Queue is full")
        return False
    else:
        queue[top_pointer] = item
        top_pointer = top_pointer + 1
        print(queue)
        return True

#question 3c: storing numbers 1 to 20
flag = False
for i in range(1, 22):
    enqueue(i)
    if i == 21:
        flag = True
if flag == True:
    print("Successful")
else:
    print("Unsuccessful")

#question 3d: recursive function
def recursive_output(start):
    if start == 0:
        return queue[start]
    else:
        return queue[start] + recursive_output(start - 1)
    
#question 3ei: call the recursive function
#question 3eii: test the program
result = recursive_output(19)
print(result)

