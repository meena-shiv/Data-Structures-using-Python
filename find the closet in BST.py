def tolist(root,l):
    if root!=None:
        tolist(root.left,l)
        l.append(root.key)
        tolist(root.right,l)
def maxDiff(root, k):
    l=[]
    tolist(root,l)
    if k in l:
        return 0
    else:
        q=100000
        for i in l:
            p=abs(k-i)
            if p<q:
                q=p
                x=p
        return x
