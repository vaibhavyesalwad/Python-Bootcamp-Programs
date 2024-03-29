
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self,num):
        new_node = Node(num)
        if self.head is None:
            self.head = new_node
            return
        n= self.head
        while n.next is not None:
            n = n.next
        n.next = new_node

    def search(self, snum):
        n = self.head
        while n and n.data != snum:
            n = n.next
        if n is None:
            return False
        else:
            return True

    def traverse(self):
        n= self.head
        while n:
            print(n.data,end='->')
            n= n.next


def store(num):
    index = num % 11
    slots[index].add(num)

def search(snum):
    index = snum % 11
    if slots[index] is None:
        return False
    else:
        s= slots[index].search(snum)
        if s:
            return str(index)
        else:
            return False



numbers = [int(i) for i in input('Enter Numbers:').split()]
slots = []

head0 = LinkedList()
slots.append(head0)
head1 = LinkedList()
slots.append(head1)
head2 = LinkedList()
slots.append(head2)
head3 = LinkedList()
slots.append(head3)
head4 = LinkedList()
slots.append(head4)
head5 = LinkedList()
slots.append(head5)
head6 = LinkedList()
slots.append(head6)
head7 = LinkedList()
slots.append(head7)
head8 = LinkedList()
slots.append(head8)
head9 = LinkedList()
slots.append(head9)
head10 = LinkedList()
slots.append(head10)

for i in numbers:
    store(i)

for slot in slots:
    if slot:
        print(f'slot {slots.index(slot)}:', end=' ')
        slot.traverse()
        print()
    else:
        print(slot)

while True:
    snum = int(input('Enter number to search:'))
    if search(snum):
        print(f'{snum} present at index {search(snum)}')
    else:
        print(f'{snum} not present')





