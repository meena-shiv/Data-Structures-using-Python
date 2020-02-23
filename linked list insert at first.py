class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.start=None


    def insertFirst(self,data):
        newNode=node(data)
        if self.start==None:
            self.start=newNode

        else:
            newNode.next=self.start
            self.start=newNode

    def viewList(self):
        if self.start==None:
            print('list is empty')
        else:
            temp=self.start
            while temp!=None:
                print(temp.data,end=' ')
                temp=temp.next

llist=LinkedList()
llist.insertFirst(10)
llist.insertFirst(11)
llist.insertFirst(12)
llist.insertFirst(13)
llist.viewList()
