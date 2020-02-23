def tolist(root,l):
    if root!=None:
        l.append(root.data)
        tolist(root.left,l)
        tolist(root.right,l)
        
def getCountOfNode(root,l,h):
    l1=[]
    tolist(root,l1)
    c=0
    for i in l1:
        if i>=l and i<=h:
            c+=1
    return c
