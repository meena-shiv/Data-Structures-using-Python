def count(node,l):
    if node:
        l[0]+=1
        count(node.left,l)
        count(node.right,l)
def size(node):
    l=[0]
    count(node,l)
    return l[0]
