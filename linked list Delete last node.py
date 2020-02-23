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
            while(temp.next!=None):
                temp=temp.next
                
            temp.next=newnode


    def deletelast(self):
        if self.start==None:
            print('list is empty')
        elif self.start.next==None:
            print('deleted is = ',self.start.data)
            self.start=None
        else:
            prev=self.start
            temp=prev.next
            while(temp.next!=None):
                prev=prev.next
                temp=temp.next
            print('deleted is = ',temp.data)
            prev.next=None

    def viewlist(self):
        temp=self.start
        while temp!=None:
            print(temp.data,end=' ')
            temp=temp.next
llist=linklist()
for i in range(int(input('enter size of link list : '))):
    llist.insertatlast(int(input('enter element : ')))

llist.viewlist()
print()

llist.deletelast()
llist.deletelast()
llist.deletelast()
llist.deletelast()
llist.deletelast()
llist.deletelast()
llist.viewlist()
