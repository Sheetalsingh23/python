class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
class CircularLinkedList:
    def __init__(self):
        self.head = None
 
    def get_node(self, index):
        if self.head is None:
            return None
        current = self.head
        for i in range(index):
            current = current.next
            if current == self.head:
                return None
        return current
 
    def get_prev_node(self, ref_node):
        if self.head is None:
            return None
        current = self.head
        while current.next != ref_node:
            current = current.next
        return current
 
    def insert_after(self, ref_node, new_node):
        new_node.next = ref_node.next
        ref_node.next = new_node
 
    def insert_before(self, ref_node, new_node):
        prev_node = self.get_prev_node(ref_node)
        self.insert_after(prev_node, new_node)
 
    def insert_at_end(self, new_node):
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
        else:
            self.insert_before(self.head, new_node)
 
    def append(self, data):
        self.insert_at_end(Node(data))
 
    def display(self):
        if self.head is None:
            return
        current = self.head
        while True:
            print(current.data, end = ' ')
            current = current.next
            if current == self.head:
                break
 
def interchange(llist, n):
    current = llist.get_node(n)
    current2 = current.next
    if current2.next != current:
        before = llist.get_prev_node(current)
        after = current2.next
        before.next = current2
        current2.next = current
        current.next = after
    if llist.head == current:
        llist.head = current2
    elif llist.head == current2:
        llist.head = current
 
 
a_cllist = CircularLinkedList()
 
data_list = input('Please enter the elements in the linked list: ').split()
for data in data_list:
    a_cllist.append(int(data))
 
n = int(input('The nodes at indices n and n+1 will be interchanged.'
              ' Please enter n: '))
 
interchange(a_cllist, n)
 
print('The new list: ')
a_cllist.display()
