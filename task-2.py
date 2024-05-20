class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def find_minimum_value(root):
    if root is None:
        return None
    
    current_node = root
    while current_node.left is not None:
        current_node = current_node.left
    
    return current_node.val

root = TreeNode(20)
root.left = TreeNode(10)
root.right = TreeNode(30)
root.left.left = TreeNode(5)
root.left.right = TreeNode(15)

min_value = find_minimum_value(root)
print(f"The minimum value in the tree is: {min_value}")
