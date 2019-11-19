
class Node:
    def __init__(self,data):
        self.data= data
        self.next= None


class CircularLinkedList:
    def __init__(self):
        self.head= None

    def traverse_list(self):
        if self.head is None:
            print('Empty cicular list')
            return
        n= self.head
        while n.next is not self.head:
            print(n.data,end='->')
            n= n.next
        print(n.data)

    def insert_at_end(self,data):
        new_node= Node(data)
        if self.head is  None:
            self.head= Node(data)
            return
        n= self.head
        while n.next is self.head:
            n= n.next
        n.next= new_node
        new_node.next= self.head

    def insert_at_start(self):
        new_node= Node(data)
        new_node.next= self.head
        self.head= new_node




mylist = CircularLinkedList()

while True:
    print('''Enter your choice:
                  1. Traverse list 
                  2. Insert at end
                  X. Exit''')
    choice= input('>')
    if choice=='1':
        mylist.traverse_list()

    elif choice=='2':
        data= input('Enter data to insert:')
        mylist.insert_at_end(data)

    elif choice in 'xX':
        break