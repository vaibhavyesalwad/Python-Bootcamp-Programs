"""Create Stack data structure using class and implement push, pop and peek methods"""


class Stack:
    def __init__(self, s):
        self.size = s
        self.top = -1
        self.arr = []

    def push(self, item):
        if self.top == self.size-1:
            print('Stack full')
            return
        self.arr.append(item)
        print(f'{item} pushed')
        self.top += 1

    def pop(self):
        if self.top == -1:
            print('Empty stack')
            return
        print(f'{self.arr.pop()} removed')
        self.top -= 1

    def peek(self):
        if self.top == -1:
            print('Empty stack so no top')
            return
        print(self.arr[self.top])

    def travese(self):
        if self.top == -1:
            print('Empty stack')
            return
        print('Top')
        for i in self.arr[::-1]:
            print(i)


while True:
    try:
        size = int(input('Enter size of stack:'))
        if size < 1:
            raise Exception
        else:
            break
    except ValueError:
        print('Please enter numeric value for size of stack')
    except Exception:
        print('size value must be non-zero positive number')

mystack = Stack(size)

while True:
    print('''
    Enter your choice:
    1. Push 
    2. Pop
    3. Peek
    4. Traverse stack
    5. Exit
    ''')

    choice = input(':>')
    if choice == '1':
        data = input('Enter data to push:')
        mystack.push(data)

    elif choice == '2':
        mystack.pop()

    elif choice == '3':
        mystack.peek()

    elif choice == '4':
        mystack.travese()

    elif choice == '5':
        break

    else:
        print('Invalid choice')






