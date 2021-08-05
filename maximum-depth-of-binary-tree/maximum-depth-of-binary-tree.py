# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        def get_depth(node, depth):
            if node is None:
                return depth
            
            depth += 1
            
            return max(get_depth(node.left, depth),get_depth(node.right, depth))
        
        return get_depth(root, 0)