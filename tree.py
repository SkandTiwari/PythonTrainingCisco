class Node:
    def __init__(self, n):
        self.left = None
        self.right = None
        self.data = n

def print_tree(root):
    if root == None:
        return None
    
    print(root.data, end=": ")
    if root.left != None:
        print("L", root.left.data, end=" ")
    if root.right != None:
        print("R", root.right.data, end = " ")
    print()
    print_tree(root.left)
    print_tree(root.right)


e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(5)

e1.left = e2
e1.right = e3
e3.right = e4
print_tree(e1)



