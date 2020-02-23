def printLevelOrder(root): 
    if root is None: 
        return
    
    queue.append(root) 
  
    while(len(queue) > 0):
        
        print(queue[0].data)
        
        node = queue.pop(0) 
  
        if node.left is not None: 
            queue.append(node.left) 
  
        if node.right is not None: 
            queue.append(node.right)
