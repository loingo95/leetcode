# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
            
        def recur_reorder(node):
            if node.next is None:
                return node
            
            tail = recur_reorder(node.next)
            
            if not tail or \
                self.current_node == tail or \
                self.current_node.next == tail:
                return
            
            origin_next = self.current_node.next
            self.current_node.next = tail
            tail.next = origin_next
            self.current_node = origin_next
            
            node.next = None
            return node
        
        self.current_node = head
        recur_reorder(head)
        