# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        upper_limit = float("inf")
        lower_limit = float("-inf")
        return self.recursiveChecking(root, upper_limit, lower_limit)
    
    def recursiveChecking(self, node: TreeNode, upper_limit, lower_limit) -> bool:
        if node is None:
            return True
        
        if node.val >= upper_limit:
            return False
        
        if node.val <= lower_limit:
            return False

        return self.recursiveChecking(node.left, node.val, lower_limit) and \
            self.recursiveChecking(node.right, upper_limit, node.val)
    