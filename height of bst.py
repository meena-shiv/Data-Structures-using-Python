def height(bst):
    if isempty(bst):
        return 0
    else:
        return 1 + max(height(bst.left), height(bst.right))

'''
def maxDepth(node): 
    if node is None: 
        return 0 ;  
  
    else : 
  
        # Compute the depth of each subtree 
        lDepth = maxDepth(node.left) 
        rDepth = maxDepth(node.right) 
  
        # Use the larger one 
        if (lDepth > rDepth): 
            return lDepth+1
        else: 
            return rDepth+1
'''
