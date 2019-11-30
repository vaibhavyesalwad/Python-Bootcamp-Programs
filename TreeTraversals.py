
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def PreOrder(root):
    if root:
        print(root.data, end=' ')
        PreOrder(root.left)
        PreOrder(root.right)

def InOrder(root):
    if root:
        InOrder(root.left)
        print(root.data, end=' ')
        InOrder(root.right)

def PostOrder(root):
    if root:
        PostOrder(root.left)
        PostOrder(root.right)
        print(root.data, end=' ')

root= Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right = Node(5)

print('InOrder:', end= '')
InOrder(root)
print('\nPreOrder:', end='')
PreOrder(root)
print('\nPostOrder:', end='')
PostOrder(root)


