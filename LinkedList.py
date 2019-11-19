class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def traverse_list(self):
        if self.head is None:
            print('Empty linked list')
            return
        n = self.head
        while n is not None:
            print(n.data, end='->')
            n = n.next
        print()

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print('New node inserted at start')

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            n = n.next
        n.next = new_node
        print('New node inserted at end')

    def insert_at_position(self, pos, data):
        new_node = Node(data)
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            print('Element inserted at start')
            return
        i = 1
        n = self.head
        while i < pos - 1 and n is not None:
            n = n.next
            i += 1
        if n is None:
            print('Index outbound')
            return
        new_node.next = n.next
        n.next = new_node
        print(f'New node added at position {pos}')

    def delete_at_start(self):
        if self.head is None:
            print('Empty list so no element to delete')
            return
        self.head = self.head.next
        print('First node deleted')

    def delete_at_end(self):
        if self.head is None:
            print('Empty list so no elements to delete')
            return
        n = self.head
        while n.next.next is not None:
            n = n.next
        n.next = None
        print('Last node deleted')

    def delete_at_position(self, pos):
        if self.head is None:
            print('Empty list so no element to delete')
            return
        i = 1
        if pos == 1:
            self.head = self.head.next
            print('First node deleted')
            return
        n = self.head
        while i < pos - 1:
            n = n.next
            i += 1
        n.next = n.next.next
        print(f'Node at position {pos} deleted')


mylist = LinkedList()
yourlist = LinkedList()

while (True):
    print('\nEnter your choice:\n' \
          '1.Traverse list\n' \
          '2.Insert node at start\n' \
          '3.Insert node at end\n' \
          '4.Insert node at position\n' \
          '5.Delete node at start\n' \
          '6.Delete node at end\n' \
          '7.Delete node at position\n' \
          '8.Exit')

    choice = input('>')
    if choice == '1':
        mylist.traverse_list()
    elif choice == '2':
        data = input('Enter element to add at start:')
        mylist.insert_at_start(data)
    elif choice == '3':
        data = input('Enter element to add at end:')
        mylist.insert_at_end(data)
    elif choice == '4':
        pos = int(input('Enter position of node to insert:'))
        data = input('Enter element to be added:')
        mylist.insert_at_position(pos, data)
    elif choice == '5':
        mylist.delete_at_start()
    elif choice == '6':
        mylist.delete_at_end()
    elif choice == '7':
        pos = int(input('Enter position of node to delted::'))
        mylist.delete_at_position(pos)
    elif choice == '8':
        break
    else:
        print('Invalid choice')









