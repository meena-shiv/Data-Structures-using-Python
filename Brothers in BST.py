def tolist1(root1,l):
    if root1!=None:
        tolist1(root1.left,l)
        l.append(root1.data)
        tolist1(root1.right,l)
def tolist2(root2,l1):
    if root2!=None:
        tolist2(root2.left,l1)
        l1.append(root1.data)
        tolist2(root2.right,l1)
        
def countPairs(root1, root2, x):
    l=[]
    l1=[]
    tolist1(root1,l)
    tolist1(root2,l1)
    p=0
    for i in l:
        for j in l1:
            if i+j==x:
                p+=1
    return p
