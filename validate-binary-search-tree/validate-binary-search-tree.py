# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.recursiveChecking(root)
    
    def recursiveChecking(self, node: TreeNode) -> bool:
        if node is None:
            return True
            
        if not (self.check_left_subtree(node, node.left) and
            self.check_right_subtree(node, node.right)):
            return False
        
        return self.recursiveChecking(node.left) and \
            self.recursiveChecking(node.right)
    
    
    def check_left_subtree(self, root, node) -> bool:
        if node is None:
            return True
        
        if node.val >= root.val:
            return False
        
        return self.check_left_subtree(root, node.left) and \
            self.check_left_subtree(root, node.right)
        
    def check_right_subtree(self, root, node) -> bool:
        if node is None:
            return True
        
        if node.val <= root.val:
            return False
        
        return self.check_right_subtree(root, node.left) and \
            self.check_right_subtree(root, node.right) 