class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linklist:
    def __init__(self):
        self.start=None


    def insertatlast(self,data):
        newnode=node(data)
        if self.start==None:
            self.start=newnode

        else:
            temp=self.start
            while temp.next!=None:
                temp=temp.next
            temp.next=newnode

    def viewlist(self):
        if self.start==None:
            print('listnis empty')
        else:
            temp=self.start
            while temp!=None:
                print(temp.data)
                temp=temp.next

    def deletegivenpos(self,pos):
        k=2
        if pos==1:
            self.start=self.start.next
        
        else:
            temp=self.start
            ntemp=temp.next
            while k!=pos:
                temp=temp.next
                ntemp=temp.next
                k+=1
            print('deleted is ',ntemp.data)
            temp.next=ntemp.next
                
            

llist=linklist()
print('enter elements to list : ')
l=[int(i) for i in input().split()]
for i in l:
    llist.insertatlast(i)
llist.viewlist()
print()
llist.deletegivenpos(4)
print()
llist.viewlist()
            
            
