class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def sum_of_values(root):
    if root is None:
        return 0
    return root.val + sum_of_values(root.left) + sum_of_values(root.right)

root = TreeNode(20)
root.left = TreeNode(10)
root.right = TreeNode(30)
root.left.left = TreeNode(5)
root.left.right = TreeNode(15)

total_sum = sum_of_values(root)
print(f"The sum of all values in the tree is: {total_sum}")
