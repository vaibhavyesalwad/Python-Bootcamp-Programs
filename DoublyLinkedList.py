
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def traverse(self):
        if self.head is None:
            print('Empty Doubly Linked List')
            return
        n = self.head
        print('head',end= ' ')
        while(n):
            if n.next is None:
                print(n.data, end=' ')
            else:
                print(n.data,end='<->')
            n = n.next
        print(' tail')


    def traverse_reverse(self):
        if self.head is None:
            print('Empty Doubly Linked List')
            return
        n= self.tail
        print('tail',end=' ')
        while n:
            if n.prev is not None:
                print(n.data,end='<->')
            else:
                print(n.data,end=' ')
            n = n.prev
        print('head')



    def insert_first(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            print(f'{data} inserted as first and last node')
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        print(f'{data} inserted as first node')


    def insert_last(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            print(f'{data} inserted as last and first node')
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        print(f'{data} inserted as last node')


    def delete_first(self):
        if self.head is None:
            print('Empty doubly linked list')
            return
        print(f'{self.head.data} as first node deleted')
        self.head = self.head.next
        self.head.prev = None


    def delete_last(self):
        if self.head is None:
            print('Empty doubly linked list no node to delete')
            return
        elif self.head.next is None:
            print(f'{self.head.data} single node in list deleted now empty list')
            self.head = None
            self.tail = None
            return
        print(f'{self.tail.data} last node deleted')
        self.tail = self.tail.prev
        self.tail.next = None


    def insert_at_position(self,pos,data):
        new_node = Node(data)
        if pos == 1:
            if self.head is None:
                self.head = new_node
                self.tail = new_node
                print(f'{data} inserted as first and last node')
                return
        n = self.head
        i = 1
        while n and i < pos-1:
            n = n.next
            i += 1
        if n is None:
            print('Index outbound')
            return
        if n.next is None:
            new_node.prev = n
            n.next = new_node
            self.tail = new_node
            print(f'{data} inserted as tail node')
            return
        new_node.prev = n
        new_node.next = n.next
        n.next = new_node
        new_node.next.prev = new_node
        print(f'node wid {data} inserted at {pos} position')


    def delete_at_position(self,pos):
        if self.head is None:
            print('Empty Doubly Linked List')
            return
        n = self.head
        i=1
        while n and i < pos-1:
            n= n.next
        if n is None:
            print('Index outbound')
            return
        n.next = n.next.next



mylist = DoublyLinkedList()

while(True):
    print('''
    Enter your choice:
    1. Traverse Doubly List
    2. Insert node at first
    3. Insert node at last
    4. Delete first node
    5. Insert at position
    6. Traverse Reverse
    7. Exit    
    ''')
    choice = input(':>')
    if choice == '1':
        mylist.traverse()
    elif choice == '2':
        data = input('Enter data for new head:')
        mylist.insert_first(data)
    elif choice == '3':
        data = input('Enter data for new tail:')
        mylist.insert_last(data)
    elif choice == '4':
        mylist.delete_first()
    elif choice == '5':
        data = input('Enter data for node:')
        pos = int(input('Enter position of new node:'))
        mylist.insert_at_position(pos,data)
    elif choice == '6':
        mylist.traverse_reverse()
    elif choice == '7':
        break



