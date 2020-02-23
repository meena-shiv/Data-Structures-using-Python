def height(root):
if root==None:
    return 0
return 1+max(height(root.left) , height(root.right))
