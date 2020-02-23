def sumofleaf(root,l):
    if root!=None:
        if root.left==None and root.right==None:
            l.append(root.data)
        sumofleaf(root.left,l)
        sumofleaf(root.right,l)

def sumOfLeafNodes(root):
    l=[]
    sumofleaf(root,l)
    return sum(l)
