# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.compare(root.left, root.right)
        
    def compare(self, node_1, node_2):
#         if code can reach the leave the it's true
        if (node_1 is None) and (node_2 is None):
            return True
#         if either of node is none and other one is a leaf then it's false
        if (node_1 is None) or (node_2 is None):
            return False
#         if current nodes is not equal return immediately
        if node_1.val != node_2.val:
            return False
#         All sub compare must be true to return a true value
        return self.compare(node_1.left, node_2.right) and self.compare(node_1.right, node_2.left)
        
        
        