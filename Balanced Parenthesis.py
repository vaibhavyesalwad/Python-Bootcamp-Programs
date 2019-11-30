
class Stack:
    def __init__(self):
        self.top = -1
        self.arr = []

    def operate(self, ch):
        if ch == '(':
            self.arr.append(ch)
            self.top += 1
        elif ch == ')':
            self.arr.pop()
            self.top -= 1


expression= input('Enter mathematical expression:')

mystack = Stack()

for ch in expression:
    mystack.operate(ch)

if mystack.top == -1:
    print(f'{expression} is a balanced expression')
else:
    print(f'{expression} is not balanced expression')
