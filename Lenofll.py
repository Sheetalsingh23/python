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
 
    def length(self):
        return self.length_helper(self.head)
 
    def length_helper(self, current):
        if current is None:
            return 0
        return 1 + self.length_helper(current.next)
 
a_llist = LinkedList()
data_list = input('Please enter the elements in the linked list: ').split()
for data in data_list:
    a_llist.append(int(data))
 
print('The length of the linked list is ' + str(a_llist.length()) + '.', end = '')
