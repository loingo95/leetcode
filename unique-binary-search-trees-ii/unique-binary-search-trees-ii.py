# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
#         # First ideal
#         if n == 1:
#             return TreeNode(1)
        
#         sub_trees = self.generateTrees(n - 1) # List[TreeNode]
        
#         n_trees = []
#         # append current n to head of each sub trees
#         for tree in sub_trees:
#             n_node = TreeNode(val=n, left=tree)
#             n_trees.append(n_node)
            
#         # PROBLEM: how can we clone identical trees
#         def recur_n_to_right(node):
#             n_node = TreeNode(val=n, left=tree)
#             if not node.right:
#                 node.right = n_node
#                 count ++
            
#             n_node.left = node.right
#             node.right = n_node
#             count ++
#             recur_n_to_right(node.right)

        def generate_tree_in_range(i, j):
            if j<i:
                return [None]
            elif j==i:
                return [TreeNode(i)]
            
            
            res = []
            for k in range(i, j+1):
                lefts = generate_tree_in_range(i, k-1)
                rights = generate_tree_in_range(k+1, j)
                for left in lefts:
                    for right in rights:
                        root = TreeNode(k)
                        root.left = left
                        root.right = right
                        res.append(root)
                        
            return res
        
        
        if n == 0:
            return []
        
        return generate_tree_in_range(1, n)
            
            
            
            