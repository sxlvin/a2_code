
#Question 3a: declare 2D array & initialise
array_nodes = [[ -1 for i in range(0, 3)] for j in range(0, 20)]
left_pointer = -1
data = -1
right_pointer = -1

#Question 3b: storing the data
free_node = 6
root_pointer = 0

array_nodes[0][0], array_nodes[0][1], array_nodes[0][2] = 1, 20, 5
array_nodes[1][0], array_nodes[1][1], array_nodes[1][2] = 2, 15, -1
array_nodes[2][0], array_nodes[2][1], array_nodes[2][2] = -1, 3, 3
array_nodes[3][0], array_nodes[3][1], array_nodes[3][2] = -1, 9, 4
array_nodes[4][0], array_nodes[4][1], array_nodes[4][2] = -1, 10, -1
array_nodes[5][0], array_nodes[5][1], array_nodes[5][2] = -1, 58, -1
array_nodes[6][0], array_nodes[6][1], array_nodes[6][2] = -1, -1, -1

print(array_nodes)

#Question 3c: seacrhvalue()
def search_value(root, value_to_find):
    if root == -1:
        return -1
    else:
        if array_nodes[root][1] == value_to_find:
            return root
        else:
            if array_nodes[root][1] == -1:
                return -1
            
    if array_nodes[root][1] > value_to_find:
        return search_value(array_nodes[root][0], value_to_find)
    
    if array_nodes[root][1] < value_to_find:
        return search_value(array_nodes[root][2], value_to_find)

print(search_value(root_pointer, 15))

#Question 3d: post_order()
def post_order(root_pointer):
    if array_nodes[root_pointer][0] != -1:
        post_order(array_nodes[root_pointer][0])
    if array_nodes[root_pointer][2] != -1:
        post_order(array_nodes[root_pointer][2])
    print(str(array_nodes[root_pointer][1]))

print(post_order(root_pointer))

#Question 3ei: call the functions
#Question 3eii: test the program