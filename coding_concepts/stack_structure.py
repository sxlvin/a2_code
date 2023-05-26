
#code for stack
stack = [""]*10
top_pointer = -1
base_pointer = 0
stack_full = len(stack)
item = ""

def push(item):
    global top_pointer
    if top_pointer == stack_full:
        print("Stack full!")
    else:
        stack[top_pointer + 1] = item
        top_pointer = top_pointer + 1

def pop():
    global top_pointer, item
    if top_pointer < base_pointer:
        print("Stack full!")
    else:
        stack[top_pointer] = item
        top_pointer = top_pointer -1

def print_stack():
    print(stack)

print_stack()
push(8)
push(9)
push(10)
print_stack()
pop()
pop()
print_stack()