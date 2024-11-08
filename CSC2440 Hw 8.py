#Jayden
class Node:
    def __init__(self, v):
        self.value = v
        self.left = None
        self.right = None

def InsertPreorder(root, v):
    if root is None:
        return Node(v)

    if root.left is None:
        root.left = Node(v)

    elif root.right is None:
        root.right = Node(v)

    else:
        InsertPreorder(root.left, v)

    if root.left is not None and root.right is None:
        root.right = Node(v)

    return root

def DisplayPostorder(root):
    if root is None:
        return

    DisplayPostorder(root.left)
    DisplayPostorder(root.right)
    print(root.value, end=' ')

if __name__ == "__main__":
    root = Node(2)
    root.left = Node(3)
    root.right = Node(4)
    root.left.left = Node(5)

    InsertPreorder(root, 6)

    print("Postorder traversal:")
    DisplayPostorder(root)
