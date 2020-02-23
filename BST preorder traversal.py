class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
        
def insert(root,node):
    if root==None:
        root=node
    else:
        if root.data<node.data:
            if root.right==None:
                root.right=node
            else:
                insert(root.right,node)
        elif root.data>node.data:
            if root.left==None:
                root.left=node
            else:
                insert(root.left,node)
                
                
def preorder(root,l1):
    if root!=None:
        l1.append(root.data)
        preorder(root.left,l1)
        preorder(root.right,l1)
        
for i in range(int(input())):
    a=int(input())
    l=[int(i) for i in input().split()]
    root=node(l[0])
    for i in range(1,a):
        insert(root,node(l[i]))
        
    l1=[]
    preorder(root,l1)
    
    if l==l1:
        print(1)
        
    else:
        print(0)
    
    
    
    
    
    
    
    
    
            
        
