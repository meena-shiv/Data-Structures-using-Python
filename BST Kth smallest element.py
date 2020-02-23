def tolist(root,l):
    if root==None:
        return
    tolist(root.left,l)
    l.append(root.data)
    tolist(root.right,l)
        
def k_smallest_element(root, n):
    l=[]
    tolist(root,l)
    return l[n-1]
