# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.smallests = [float("inf")]*k
        self.find_with_inorder_traversal(root)
            
        return self.smallests[-1]
    
    def update_smallest(self, node):
        if node and node.val < self.smallests[-1]:
            self.smallests[-1] = node.val
            self.smallests = sorted(self.smallests)

    def find_with_inorder_traversal(self, node):
        if node is None:
            return
        if node:
            self.find_with_inorder_traversal(node.left)
            self.update_smallest(node)
            self.find_with_inorder_traversal(node.right)
