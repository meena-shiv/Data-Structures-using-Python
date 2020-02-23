def tomodify(root,l):
    if root!=None:
        tomodify(root.right,l)
        l[0]=l[0]+root.data
        root.data=l[0]
        tomodify(root.left,l)
        
        
def modifyBST(root):
    l=[0]
    tomodify(root,l)

class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
def insert(root, node):
    if root is None:
        root = node
    else:
        if root.data < node.data:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        elif root.data == node.data:
            return
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)
def traverseInorder(root):
    if root is not None:
        traverseInorder(root.left)
        print(root.data, end=" ")
        traverseInorder(root.right)
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        root = None
        for j in arr:
            if root is None:
                root = Node(j)
            else:
                insert(root, Node(j))
        modifyBST(root)
        traverseInorder(root)
        print('')
# Contributed by: Harshit Sidhwa
