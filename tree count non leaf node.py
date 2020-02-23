def tonode(root,l):
    if root:
        if root.left!=None or root.right!=None:
            l[0]+=1
        tonode(root.left,l)
        tonode(root.right,l)
        
def countNonLeafNodes(root):
    l=[0]
    tonode(root,l)
    return l[0]
