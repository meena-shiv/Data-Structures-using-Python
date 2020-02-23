def tolist(root,l):
    if root!=None:
        tolist(root.left,l)
        l.append(root.data)
        tolist(root.right,l)
def isBST(root):
    l=[]
    tolist(root,l)
    p=sorted(l)
    if p==l:
        return 1
    else:
        return 0
