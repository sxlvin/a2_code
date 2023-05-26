
#Question 1a: decalre array and pointers
stack = [""]*10
top_pointer = -1
end_pointer = 0
stack_full = len(stack) - 1
item = ""

#Question 1b: output all 10 elements and value of stackpointer
def print_stack():
    global stack, end_pointer
    print("This is the stack: ", stack)
    print("This is the start pointer: ", end_pointer)

#Question 1c: push() function
#Question 1di: modify the code
#Question 1dii: test the program
def push(item):
    global top_pointer
    if top_pointer < stack_full:
        stack[top_pointer + 1] = item
        top_pointer = top_pointer + 1
        return True
    elif top_pointer == stack_full:
        return False

for i in range(0, 11):
    number = int(input("Please enter a number: "))
    if i != 10:
        push(number)
        print("Number added")
        print(stack)
    else:
        print("Number not added")
        print(stack)

#Question 1ei: pop()
def pop():
    global top_pointer, end_pointer, item
    if top_pointer < end_pointer:
        return -1
    else:
        temp = stack[top_pointer]
        stack[top_pointer] = item
        top_pointer = top_pointer - 1
        return temp

#Question 1eii: pop twice and print stack
print(pop())
print(pop())
print(stack)
