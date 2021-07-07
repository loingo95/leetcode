# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        nodeIds = []
        current = head
        while current is not None:
            current_id = id(current)
            if current_id in nodeIds:
                return True
            nodeIds.append(current_id)
            current = current.next
            
        return False
