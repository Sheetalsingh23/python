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
        while current:
            print(current.data, end = ' ')
            current = current.next
 
 
def reverse_llist(llist, n):
    if n == 0:
        return
    before = None
    current = llist.head
    if current is None:
        return
    after = current.next
    for i in range(n):
        current.next = before
        before = current
        current = after
        if after is None:
            break
        after = after.next
    llist.head.next = current
    llist.head = before
 
 
a_llist = LinkedList()
 
data_list = input('Please enter the elements in the linked list: ').split()
for data in data_list:
    a_llist.append(int(data))
n = int(input('Enter the number of elements you want to reverse in the list: '))
 
reverse_llist(a_llist, n)
 
print('The new list: ')
a_llist.display()
