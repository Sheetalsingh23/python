
Program/Source Code
Here is the source code of a Python program to find the smallest and largest elements in a binary search tree. The program output is shown below.

class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
 
    def insert(self, node):
        if self.key > node.key:
            if self.left is None:
                self.left = node
                node.parent = self
            else:
                self.left.insert(node)
        elif self.key < node.key:
            if self.right is None:
                self.right = node
                node.parent = self
            else:
                self.right.insert(node)
 
    def search(self, key):
        if self.key > key:
            if self.left is not None:
                return self.left.search(key)
            else:
                return None
        elif self.key < key:
            if self.right is not None:
                return self.right.search(key)
            else:
                return None
        return self
 
 
class BSTree:
    def __init__(self):
        self.root = None
 
    def add(self, key):
        new_node = BSTNode(key)
        if self.root is None:
            self.root = new_node
        else:
            self.root.insert(new_node)
 
    def search(self, key):
        if self.root is not None:
            return self.root.search(key)
 
    def get_smallest(self):
        if self.root is not None:
            current = self.root
            while current.left is not None:
                current = current.left
            return current.key
 
    def get_largest(self):
        if self.root is not None:
            current = self.root
            while current.right is not None:
                current = current.right
            return current.key
 
 
bstree = BSTree()
 
print('Menu (this assumes no duplicate keys)')
print('add <key>')
print('smallest')
print('largest')
print('quit')
 
while True:
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
    if operation == 'add':
        key = int(do[1])
        bstree.add(key)
    if operation == 'smallest':
        smallest = bstree.get_smallest()
        print('Smallest element: {}'.format(smallest))
    if operation == 'largest':
        largest = bstree.get_largest()
        print('Largest element: {}'.format(largest))
    elif operation == 'quit':
        break
