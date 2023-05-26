
#binary tree: data structure where each node is allowed to have two child nodes

class tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.count = 1
    
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left == None:
                    self.left = tree(data)
                else: 
                    self.left.insert(data)
            else:
                if self.right == None:
                    self.right = tree(data)
                else: 
                    self.right.insert(data)
        else:
            self.data = data

        self.count += 1

    def total(self):
        return self.count

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

    def search(self, item):
        if item < self.data:
            if self.left == None:
                return "Item not found"
            return self.left.search(item)
        
        if item > self.data:
            if self.right == None:
                return "Item not found"
            return self.right.search(item)
        
        else:
            return "Data found"


mytree = tree(12)
mytree.insert(90)
mytree.insert(1)
mytree.insert(77)
mytree.insert(7)
mytree.insert(82)

print("number of elements:", mytree.total())
mytree.print_tree()
print(mytree.search(77))