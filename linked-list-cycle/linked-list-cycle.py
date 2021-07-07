# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
##        Here is my first implement
#         nodeIds = []
#         current = head
#         while current is not None:
#             current_id = id(current)
#             if current_id in nodeIds:
#                 return True
#             nodeIds.append(current_id)
#             current = current.next
            
#         return False

        # Here is a more adhoc version base on assumption that
        # The number of the nodes in the list is in the range [0, 104]
        for i in range(0, 10**4 + 1):
            if head is None:
                return False
            head = head.next
        return True
