class Node:
    #Constructer
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

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

# Function to delete Item in the BST
def delete_node(key, num):
    if key is None:
        return num
    if key.val > num:
        key.left = delete_node(key.left,num)
        return key
    elif key.val < num:
        key.right = delete_node(key.right,num)
        return key
    
    if key.left is None:
        temp = key.right
        del key
        return temp
    elif key.right is None:
        temp = key.left
        del key
        return temp
    else:
        parent = key

        succ = key.right
        while succ.left is not None:
            parent = succ
            succ = succ.left

        if parent != key:
            parent.left = succ.right
        else:
            parent.right = succ.right
        
        key.key = succ.key

        del succ
        return key


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

#Function to delete the deepest node in  binary tree

#Loop to input numbers into the binary tree
y = Node(70)
while True:
    num = int(input("\n\tEnter an Integer to add to BST e.g 25 ===> "))
    if num == 0:
        break
    y = insert(y,num)

answer = 10
print()
for x in range(60):
    print("-", end = '')

while answer != 7:
    print("\n\n\tSelect from any of these options:",
        "\n\n\t1:   Print BST in PostOrder",
        "\n\t2:   Print Largest Item in BST",
        "\n\t3:   Print Smallest Item in BST",
        "\n\t4:   Print a list of Prime numbers in the BST",
        "\n\t5:   Print the Sum of all Items in the BST",
        "\n\t6:   Delete an item from the BST",
        "\n\t7:   End Program")
    answer = int(input("\n\t\tEnter Number ===> "))
    for x in range(60):
        print("-", end = '')
    print()
    if answer == 1:
        print("\n\t\tPostorder Traversal: ", end = '')
        postorder(y)
    elif answer == 2:
        print("\n\t\tLargest Element: ", find_largest(y))
    elif answer == 3:
        print("\n\t\tSmallest Element: ", find_smallest(y))
    elif answer == 4:
        print("\n\t\tPrime Numbers:", end = '')
        primeinTree(y)
    elif answer == 5:
        print("\n\t\tSum of all Items:", end = '')
        find_sum(y)
    elif answer == 6:
        print("\n\t\tWhich item would you like to delete from the BST?  ===> ", end='')
        userNum = int(input())
        delete_node(y,userNum)
    print()
    for x in range(2):
        print()
        for j in range(60):
            print("-", end = '')
    








