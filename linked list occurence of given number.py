def count(head, search_for):
    temp=head
    p=0
    while temp!=None:
        if temp.data==search_for:
            p+=1
        temp=temp.next
   
    return p
