# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        head_next = head.next
        head.next = None
        new_head = self.recurse(head, head_next)
        return new_head
        
    def recurse(self, node, node_next):
        if node_next.next is None:
            node_next.next = node
            return node_next
        
        node_next_next = node_next.next
        node_next.next = node
        
        return self.recurse(node_next, node_next_next)
        