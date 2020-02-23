def list1(root1,l):
    if root1!=None:
        l.append(root1.data)
        list1(root1.left,l)
        list1(root1.right,l)
        
def list2(root2,l1):
    if root2!=None:
        l1.append(root2.data)
        list2(root2.left,l1)
        list2(root2.right,l1)  
        
        
def printCommon(root1, root2):
    l,l1=[],[]
    list1(root1,l)
    list2(root2,l1)
    l2=[]
    l=set(l)
    l=sorted(l)
    for i in l:
        if i in l1:
            print(i,end=' ')
