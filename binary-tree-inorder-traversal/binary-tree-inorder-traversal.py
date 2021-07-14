# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        values = []
        self._inorderTraversal(root, values)
        return values
        
    def _inorderTraversal(self, node: TreeNode, values: List) -> Optional[int]:
        if node is None:
            return
        
        self._inorderTraversal(node.left, values)
        values.append(node.val)
        self._inorderTraversal(node.right, values)