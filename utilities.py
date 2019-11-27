
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class List:
    def __init__(self):
        self.head = None
        print(f'New empty list created')

    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def add(self,item):
        if not self.search(item):
            new_node = Node(item)
            if self.isEmpty():
                self.head = new_node
                print(f'{item} added to list')
                return
            new_node.next = self.head
            self.head = new_node
            print(f'{item} added to list')
        else:
            print(f'{item} already present in the list')

    def search(self,item):
        if self.isEmpty():
            return False
        n = self.head
        while n and n.data != item:
            n = n.next
        if n is None:
            return False
        else:
            return True

    def size(self):
        n = self.head
        i = 0
        while n:
            n= n.next
            i += 1
        return i

    def append(self, item):
        if not self.search(item):
            new_node = Node(item)
            if self.isEmpty():
                self.head = new_node
                print(f'{data} added at end of list')
                return
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node
            print(f'{item} added at end of list')

    def index(self,data):
        if self.search(data):
            n = self.head
            i = 1
            while n.data != data:
                n= n.next
                i += 1
            return i
        else:
            return 'Item not present in the list'

    def insert(self, pos, item):
        if not self.search(item):
            new_node = Node(item)
            if pos == 1:
                new_node.next = self.head
                self.head = new_node
                print(f'{item} added at position {pos}')
                return
            i = 1
            n = self.head
            while n and i < pos-1:
                n = n.next
                i += 1
            if n.next is None:
                n.next = new_node
                print(f'{item} added at position {pos}')
                return
            elif n is None:
                print('Index outbound')
                return
            new_node.next = n.next
            n.next = new_node
            print(f'{item} added at position {pos}')
        else:
            print(f'{item} is already present so not added')

    def remove(self, item):
        if self.search(item):
            n = self.head
            while n and n.next.data != item:
                n = n.next
            print(f'{item} removed from list')
            n.next = n.next.next
        else:
            print(f'{item} not present in the list')

    def pop(self, pos = 0):
        if self.isEmpty():
            print('List is empty')
            return
        elif pos == 0:
            if self.head.next is None:
                print(f'{self.head.data} first and last element deleted')
                self.head = None
                return
            n = self.head
            while n.next.next is not None:
                n = n.next
            print(f'Last element {n.next.data} deleted')
            n.next = None
            return
        if pos == 1:
            print(f'First element {self.head.data} deleted')
            self.head = self.head.next
            return
        n = self.head
        i = 1
        while n and i < pos-1:
            n = n.next
            i += 1
        if n is None:
            print('Index outbound')
            return
        print(f'Element {n.next.data} at {pos} deleted')
        n.next = n.next.next

    def traverse(self):
        if self.isEmpty():
            print('Empty list')
            return
        n = self.head
        while n:
            print(n.data, end=' ')
            n = n.next







