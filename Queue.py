
class Queue:
    def __init__(self,size):
        self.size= size
        self.rear= -1
        self.front= -1
        self.arr= []

    def enqueue(self,data):
        if self.rear==  self.size -1:
            print('Queue full')
            return

        elif self.front== -1:
            self.arr.append(data)
            print(f'{data} addded to queue')
            self.front += 1
            self.rear += 1
            return

        self.arr.append(data)
        print(f'{data} addded to queue')
        self.rear += 1

    def dequeue(self):
        if self.front== -1:
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

    def traverse_queue(self):
        if self.front == -1:
            print('Empty queue')
            return

        else:
            print('Front', end=' ')
            for i in self.arr:
                print(i, end=' ')
            print('Rear')


size= int(input('Enter size of queue:'))
myqueue= Queue(size)

while True:
    print('''
    Enter ur choice:
    1. Enqueue
    2. Dequeue
    3. Traverse Queue
    4. Exit
    ''')

    choice= input(':>')
    if choice== '1':
        data= input('Enter element to put into queue:')
        myqueue.enqueue(data)

    elif choice== '2':
        myqueue.dequeue()

    elif choice== '3':
        myqueue.traverse_queue()

    elif choice== '4':
        break

    else:
        print('Invalid choice')


