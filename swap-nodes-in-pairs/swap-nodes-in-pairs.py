# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        next_head = head.next.next
        temp = head
        head = head.next
        head.next = temp
        
        head.next.next = self.swapPairs(next_head)
        return head
        
        
        