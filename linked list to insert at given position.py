class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linklist:
    def __init__(self):
        self.start=None

    def insertfirst(self,data):
        newnode=node(data)
        if self.start==None:
            self.start=newnode
        else:
            newnode.next=self.start
            self.start=newnode

    def insertAtGivenPosition(self,pos,data):
        newnode=node(data)
        k=1
        if pos==1:
            newnode.next=self.start
            self.start=newnode


        else:
            temp=self.start
            
            while(k+1!=pos):
                temp=temp.next
                k+=1   
            newnode.next=temp.next
            temp.next=newnode
        

    def viewlist(self):
        if self.start==None:
            print('list is empty')
        else:
            temp=self.start
            while temp!=None:
                print(temp.data,end=' ')
                temp=temp.next


llist=linklist()
for i in range(int(input('enter the size of link list : '))):
    llist.insertfirst(int(input('enter elements of list at first : ')))
llist.viewlist()

x=int(input('enter position to insert : '))
y=int(input('enter element to insert : '))

llist.insertAtGivenPosition(x,y)

llist.viewlist()





