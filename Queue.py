"""Create Queue data structure using class and implement enqueue, dequeue and peak methods"""


class Queue:
    def __init__(self, s):
        self.size = s
        self.rear = -1
        self.front = -1
        self.arr = []

    def enqueue(self, data):
        if self.rear == self.size - 1:
            print('Queue full')
            return

        elif self.front == -1:
            self.arr.append(data)
            print(f'{data} addded to queue')
            self.front += 1
            self.rear += 1
            return

        self.arr.append(data)
        print(f'{data} added to queue')
        self.rear += 1

    def dequeue(self):
        if self.front == -1:
            print('Empty queue so no element to remove')
            return

        elif self.front == self.rear:
            print(f'{self.arr.pop(self.front)} removed from que')
            print('Empty queue')
            self.front -= 1
            self.rear -= 1
            return

        print(f'{self.arr.pop(self.front)} removed from queue')
        self.rear -= 1

    def traverse(self):
        if self.front == -1:
            print('Empty queue')
            return

        else:
            print('Front', end=' ')
            for i in self.arr:
                print(i, end=' ')
            print('Rear')


while True:
    try:
        size = int(input('Enter size of queue:'))
        if size < 1:
            raise Exception
        else:
            break
    except ValueError:
        print('Please enter numeric value for size of the queue')
    except Exception:
        print('size value must be non-zero positive number')

myqueue = Queue(size)

while True:
    print('''
    Enter ur choice:
    1. Enqueue
    2. Dequeue
    3. Traverse Queue
    4. Exit
    ''')

    choice = input(':>')
    if choice == '1':
        data = input('Enter element to put into queue:')
        myqueue.enqueue(data)

    elif choice == '2':
        myqueue.dequeue()

    elif choice == '3':
        myqueue.traverse()

    elif choice == '4':
        break

    else:
        print('Invalid choice')


