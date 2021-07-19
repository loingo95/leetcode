# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k_smallests = [float("inf")]*k
        self.find_with_inorder_traversal(root, lower_limit=float("-inf"))
            
        return self.get_kth_smallest()
    
    def get_kth_smallest(self):
        return self.k_smallests[-1]
    
    def update_smallest(self, node):
        if node and node.val < self.k_smallests[-1]:
            self.k_smallests[-1] = node.val
            self.k_smallests = sorted(self.k_smallests)

    def find_with_inorder_traversal(self, node, lower_limit):
#         If lower limit of a tree is already >= current kth smallest,
#         then we no longer need to iter through this tree
        if lower_limit >= self.get_kth_smallest():
            return
            
        if node is None:
            return
        
        if node:
            self.find_with_inorder_traversal(node.left, lower_limit)
            self.update_smallest(node)
            self.find_with_inorder_traversal(node.right, node.val)
