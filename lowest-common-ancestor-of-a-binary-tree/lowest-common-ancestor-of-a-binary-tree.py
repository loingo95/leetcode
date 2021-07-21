# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#     Lowest Common Ancestor of a Binary Tree
    
#     Common Ancestor of a Binary Tree (of p and q)-> what
#         how: traverst through tree `root`, check if node p and q is in `root`
#     -> Done
    
#     Lowest
#     Find all Common Ancestors of a Binary Tree (of p and q) -> find lowest in there
#         how: for each node in root check if Common Ancestor of a Binary Tree (of p and q) with root as current node
#     -> Common_Ancestors (of p and q)
    
#     How to find lowest in Common_Ancestors
#         -> to able to find lowest, we need height value compare
#         -> how to determine a node's height -> number of nodes between current node and root
#     min(ancestor.heigth): ancestor in Common_Ancestors
    
    
#     def find_if_node_is_common_ancestor(root, p, q) -> bool
# #         exhauted search
    
#     def find_all_ancestors(root, p, q) -> List[root_node, ...]:
#         root_nodes = [Node]
#         heights = [heigth]
#         foreach node in tree:
#             if find_if_node_common_ancestor() == True:
#                 root_nodes.insert(node)
#                 heights.insert(height)
                
#     def find_lowest_ancestor(root_nodes) -> lowest_node: Node:
# #             find smalest height
    
    
# #     func somewhere
# #     root
# #     find_if_node_is_common_ancestor(root, p, q) -> 
# #  class NodeWithHeight(Node):
#         height



class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.get_parent(root, None)
        
        p_ancestors = self.get_all_parents(p)
        q_ancestors = self.get_all_parents(q)
        
        for p_ancestor in p_ancestors:
            if p_ancestor in q_ancestors:
                return p_ancestor
        return None

    
    def get_parent(self, node, parent):
        if node is None:
            return
        node.parent = parent

        self.get_parent(node.left, node)
        self.get_parent(node.right, node)
        
    def get_all_parents(self, node):
        if node is None:
            return []
        return [node] + self.get_all_parents(node.parent)
            