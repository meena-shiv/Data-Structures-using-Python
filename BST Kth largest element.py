def tolist(root,l):
    if root==None:
        return 
    tolist(root.left,l)
    l.append(root.data)
    tolist(root.right,l)


def kthLargest(root, k):
    l=[]
    tolist(root,l)
    p=sorted(l,reverse=True)
    print(p[k-1])
