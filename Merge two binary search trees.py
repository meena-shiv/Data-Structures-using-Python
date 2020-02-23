def tolist1(root1,l1):
    if root1:
        tolist1(root1.left,l1)
        l1.append(root1.data)
        tolist1(root1.right,l1)
        
def tolist2(root2,l2):
    if root2:
        tolist2(root2.left,l2)
        l2.append(root2.data)
        tolist2(root2.right,l2)
        

def merge(root1, root2):
    l1=[]
    l2=[]
    tolist1(root1,l1)
    tolist2(root2,l2)
    p=l1+l2
    p.sort()
    for i in p:
        print(i,end=' ')
