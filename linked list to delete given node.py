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
         temp=self.start
         while temp!=None:
             print(temp.data,end=' ')
             temp=temp.next

    def deletegivendatanode(self,data):
        if self.start.data==data:
            self.start=self.start.next

        else:
            temp=self.start
            while temp.next.data!=data:
                temp=temp.next
            print('deleted is : ',temp.next.data)
            temp.next=temp.next.next


llist=linklist()
for i in range(int(input('enter size of list : '))):
    llist.insertatlast(int(input('enter element : ')))

llist.viewlist()
print()
llist.deletegivendatanode(int(input('enter to delete : ')))
llist.deletegivendatanode(int(input('enter to delete : ')))
llist.viewlist()

