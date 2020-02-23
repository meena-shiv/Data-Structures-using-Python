def tolist(root,l):
    if root!=None:
        tolist(root.left,l)
        l.append(root.data)
        tolist(root.right,l)
        

from itertools import combinations

def isTriplePresent(root):
    l=[]
    tolist(root,l)
    p=combinations(l,3)
    for i in p:
        if sum(i)==0:
            return 1
            break
    return 0
