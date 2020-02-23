def detectLoop(head):
    s = []
    temp = head 
    while (temp): 
        s=list(set(s))
        if (temp in s): 
            return True
        s.append(temp) 
        temp = temp.next
    return False
