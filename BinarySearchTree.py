class Node:
    #Constructer
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Will print inorder
def inorder(root):
    if root:
        inorder(root.left)
        print(" ", root.val, end='')
        inorder(root.right)

# Will print postorder
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(" ",root.val, end = '')

# Function to insert into the tree
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

# Find the smallest in the tree
def find_smallest(root_node):
    current = root_node
    if current:
        while current.left is not None:
            current = current.left
        return current.val
    
# Find the largest in the tree
def find_largest (root_node):
    current = root_node
    if current:
        while current.right is not None:
            current = current.right
        return current.val
    
# Function to find the prime numbers in the Tree
def prime(n,i=2):
    if n <= 2:
        return True if n == 2 else False
    if n % i == 0:
        return False
    if i*i > n:
        return True
    return prime(n,i+1)

#Goes through Binary Tree using prime function to find prime numbers
def primeinTree(node):
    current = y
    while current is not None:
        if prime(current.val):
            print(" ",current.val, end='')
        current = current.left
    current = y
    while current is not None:
        if prime(current.val):
            print(" ",current.val, end='')
        current = current.right

# Find the sum of all the numbers in the tree
def find_sum(root_node):
    if root_node == None:
        return 0
    return root_node.val + find_sum(root_node.left) \
                        + find_sum(root_node.right)

# Function to delete a node from the Binary Tree
def delete_node(root, item):
    if root is None:
        return root
    if root.val > item:
        root.left = delete_node(root.left, item)
    elif root.val < item:
        root.right = delete_node(root.right, item)
    else:
        if not root.right:
            return root.left
        if not root.left:
            return root.right
            temp = root.right
            min = temp.val
            while temp.left:
                temp = temp.left
                min = temp.val
            root.right = delete_node(right.right,root.val)
        return root

#Loop to input numbers into the binary tree
y = Node(70)
while True:
    num = int(input("\n\tEnter an Integer e.g 25 ===>"))
    if num == 0:
        break
    y = insert(y,num)

#Initial print of tree before user wants to erase anything
print("\n\tInorder Traversal: ", end = '')
inorder(y)
print("\n\tPostorder Traversal: ", end = '')
postorder(y)

#Loop that will continue as long as the user wants to keep deleting numbers from tree
print("\n\tWould you like to delete a node? 1 = Yes, 0 = No  ===>", end = '')
answer = int(input())
while answer == 1:
    print("\n\tEnter the Number you would like to delete: ", end ='')
    userNum = int(input())
    delete_node(y,userNum)
    print("\n\tWould you like to delete another Node? 1 = Yes , 0 = No ===>", end = ' ')
    answer = int(input())

print("\n\tInorder Traversal: ", end = '')
inorder(y)
print("\n\tPostorder Traversal: ", end = '')
postorder(y)
print("\n\tLargest Element: ", find_largest(y))
print("\tSmallest Element: ", find_smallest(y))
print("\tPrime Numbers:", end = '')
primeinTree(y)



