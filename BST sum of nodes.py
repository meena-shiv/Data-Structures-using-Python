def tosum(root,l):
    if root:
        l[0]+=root.data
        tosum(root.left,l)
        tosum(root.right,l)
        
def sumBT(root):
    l=[0]
    tosum(root,l)
    return l[0]
