
class Stack:
    def __init__(self,size):
        self.size= size
        self.top= -1
        self.arr= []

    def push(self,data):
        if self.top== self.size-1:
            print('Stack full')
            return
        self.arr.append(data)
        print(f'{data} pushed')
        self.top += 1

    def pop(self):
        if self.top== -1:
            print('Empty stack')
            return
        print(f'{self.arr.pop()} removed')
        self.top -= 1

    def peek(self):
        if self.top== -1:
            print('Empty stack')
            return
        print(self.arr[-1])


mystack= Stack(size=int(input('Enter size of stack:')))

while True:
    print('''
    Enter your choice:
    1. Push 
    2. Pop
    3. Peek
    4.Exit
    ''')

    choice= input(':>')
    if choice== '1':
        data= input('Enter data to push:')
        mystack.push(data)

    elif choice== '2':
        mystack.pop()

    elif choice== '3':
        mystack.peek()

    elif choice== '4':
        break

    else:
        print('Invalid choice')






