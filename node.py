import re

class Node:
    def __init__(self, key=None):
        self.left = None
        self.right = None
        self.val = key

    def insert(self, key):
        if self.val is None:
            self.val = key
            return

        if key < self.val:
            if self.left is None:
                self.left = Node(key)
            else:
                self.left.insert(key)
        elif key > self.val:
            if self.right is None:
                self.right = Node(key)
            else:
                self.right.insert(key)
        else:
            raise ValueError(f"Key {key} already exists")

    def traversePreOrder(self):
        print(self.val, end=' ')
        if self.left:
            self.left.traversePreOrder()
        if self.right:
            self.right.traversePreOrder()

    # Центрированный обход дерева
    def traverseInOrder(self):
        if self.left:
            self.left.traverseInOrder()
        print(self.val, end=' ')
        if self.right:
            self.right.traverseInOrder()

    # Обратный обход дерева
    def traversePostOrder(self):
        if self.left:
            self.left.traversePostOrder()
        if self.right:
            self.right.traversePostOrder()
        print(self.val, end=' ')



values=[]
string = input()
values=re.split(r'[ ,\(\)]+',string)
tree = Node()
for i in values:
    if i!='':
        tree.insert(int(i))

print('PreOrder:')
tree.traversePreOrder()
print('\nInOrder:')
tree.traverseInOrder()
print('\nPostOrder:')
tree.traversePostOrder()
