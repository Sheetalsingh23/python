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
 
 
def add_linked_lists(llist1, llist2):
    sum_llist = LinkedList()
    current1 = llist1.head
    current2 = llist2.head
    while (current1 and current2):
        sum = current1.data + current2.data
        sum_llist.append(sum)
        current1 = current1.next
        current2 = current2.next
    if current1 is None:
        while current2:
            sum_llist.append(current2.data)
            current2 = current2.next
    else:
        while current1:
            sum_llist.append(current1.data)
            current1 = current1.next
    return sum_llist
 
 
 
llist1 = LinkedList()
llist2 = LinkedList()
 
data_list = input('Please enter the elements in the first linked list: ').split()
for data in data_list:
    llist1.append(int(data))
 
data_list = input('Please enter the elements in the second linked list: ').split()
for data in data_list:
    llist2.append(int(data))
 
sum_llist = add_linked_lists(llist1, llist2)
 
print('The sum linked list: ', end = '')
sum_llist.display()
