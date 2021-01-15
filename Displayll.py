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
 
    def display_reversed(self):
        self.display_reversed_helper(self.head)
 
    def display_reversed_helper(self, current):
        if current is None:
            return
 
        self.display_reversed_helper(current.next)
        print(current.data, end = ' ')
 
a_llist = LinkedList()
n = int(input('How many elements would you like to add? '))
for i in range(n):
    data = int(input('Enter data item: '))
    a_llist.append(data)
 
print('The reversed linked list: ', end = '')
a_llist.display_reversed()
