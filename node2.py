import re

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# Вставка элемента
def insert(node, key):
    # Возвращаем новый узел, если дерево пустое
    if node is None:
        return Node(key)

    # Идем в нужное место и вставляет узел
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node

# Поиск inorder-преемника
def minValueNode(node):
    current = node
    # Найдем крайний левый лист — он и будет inorder-преемником
    while(current.left is not None):
        current = current.left
    return current

# Удаление узла
def deleteNode(root, key):
    # Возвращаем, если дерево пустое
    if root is None:
        return root

    # Найдем узел, который нужно удалить
    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif(key > root.key):
        root.right = deleteNode(root.right, key)
    else:
        # Если у узла только один дочерний узел или вообще их нет
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # Если у узла два дочерних узла,
        # помещаем центрированного преемника
        # на место узла, который нужно удалить
        temp = minValueNode(root.right)

        root.key = temp.key

        # Удаляем inorder-преемниа
        root.right = deleteNode(root.right, temp.key)

    return root


def iterativePreorder(root):
    parentStack=[]
    while root is not None or parentStack!=[]:
        if root:
            print(str(root.key), end=' ')
            parentStack.append(root)
            root=root.left
        else:
            root=parentStack.pop()
            root=root.right


def search(root, key):
    if root is None:
        print("Вершина не найдена")
    elif root.key == key:
        print("Вершина найдена")
    elif key < root.key:
        return search(root.left, key)
    else:  # key > v.value
        return search(root.right, key)


active = 1
while active:
    print("\nВведите команду:\n1-ввести дерево"
          "\n2-добавить вершину"
          "\n3-удалить вершину"
          "\n4-найти вершину"
          "\n5-закончить выполнение")
    command = int(input())
    if command == 1:
        values = []
        string = input()
        values = re.split(r'[ ,\(\)]+', string)
        tree = None
        for i in values:
            if i != '':
                tree = insert(tree, int(i))
        iterativePreorder(tree)
    elif command == 2:
        key=int(input())
        tree = insert(tree, key)
        iterativePreorder(tree)
    elif command == 3:
        key = int(input())
        deleteNode(tree, key)
        iterativePreorder(tree)
    elif command == 4:
        key = int(input())
        search(tree, key)
        iterativePreorder(tree)
    elif command == 5:
        active = 0
#8 (3 (1, 6 (4,7)), 10 (, 14(13,)))
