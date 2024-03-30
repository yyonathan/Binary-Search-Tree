class Node:
    #Constructer
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

#In-Order
def inorder(root):
    if root:
        inorder(root.left)
        print(" ", root.val, end='')
        inorder(root.right)

#Post-Order
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(" ",root.val, end = '')


#Returns Largest Elements
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root



def find_largest (root_node):
    current = root_node
    if current:
        while current.right is not None:
            current = current.right
        return current.val
def find_sum(root_node):
    if root_node == None:
        return 0
    return root_node.val + find_sum(root_node.left) \
                        + find_sum(root_node.right)






y = Node(70)
while True:
    num = int(input("\n\tEnter an Integer e.g 25 ===>"))
    if num == 0:
        break
    r = insert(r,num)

print("\n\tLargest Element")


