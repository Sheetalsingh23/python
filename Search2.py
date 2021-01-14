class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
 
    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
 
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end = ' ')
            current = current.next
 
    def find_index(self, key):
        current = self.head
 
        index = 0
        while current:
            if current.data == key:
                return index
            current = current.next
            index = index + 1
 
        return -1
 
a_llist = LinkedList()
for data in [4, -3, 1, 0, 9, 11]:
    a_llist.append(data)
print('The linked list: ', end = '')
a_llist.display()
print()
 
key = int(input('What data item would you like to search for? '))
index = a_llist.find_index(key)
if index == -1:
    print(str(key) + ' was not found.')
else:
    print(str(key) + ' is at index ' + str(index) + '.')
