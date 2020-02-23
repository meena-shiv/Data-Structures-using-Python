def isheap(root,l):
    if root:
        if root.left!=None and root.right!=None:
            if root.left.data<root.data and root.right.data>root.data:
                l[0]=1
            if root.left.data>root.data and root.right.data<root.data:
                l[0]=1
            if root.left.data>root.data and root.right.data>root.data:
                l[0]=1
        isheap(root.left,l)
        isheap(root.right,l)    
def isHeap(root):
    l=[0]
    isheap(root,l)
    if l[0]==1:
        return 0
    else:
        return 1
    
