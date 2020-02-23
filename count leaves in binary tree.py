def leaves(root,l):
    if root:
        leaves(root.left,l)
        if root.left==None and root.right==None:
            l[0]+=1
        leaves(root.right,l)
def countLeaves(root):
    l=[0]
    leaves(root,l)
    return l[0]
