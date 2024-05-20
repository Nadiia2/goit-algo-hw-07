class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def find_maximum_value(root):
    if root is None:
        return None
    
    current_node = root
    while current_node.right is not None:
        current_node = current_node.right
    
    return current_node.val

root = TreeNode(20)
root.left = TreeNode(10)
root.right = TreeNode(30)
root.right.left = TreeNode(25)
root.right.right = TreeNode(40)

max_value = find_maximum_value(root)
print(f"The maximum value in the tree is: {max_value}")
