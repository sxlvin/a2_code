
#code for queue
queue = [""]*10
top_pointer = 0
base_pointer = 0
queue_full = len(queue) - 1
item = ""

def enqueue(item):
    global top_pointer
    if top_pointer < queue_full:
        queue[top_pointer] = item
        top_pointer = top_pointer + 1
    else:
        print("Queue is full!")

def dequeue():
    global base_pointer, item
    if top_pointer == base_pointer:
        print("Queue is empty!")
    else:
        queue[base_pointer] = item
        base_pointer = base_pointer + 1

def print_queue():
    print(queue)

print_queue()
enqueue(8)
enqueue(9)
enqueue(10)
print_queue()
dequeue()
dequeue()
print_queue()
