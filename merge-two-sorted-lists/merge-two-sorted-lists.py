# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # base cases
        if (l1 is None) and (l2 is None):
            return None
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        
        # Init phase
        if l1.val >= l2.val:
            head = l2
            l2 = l2.next
        else:
            head = l1
            l1 = l1.next
        current_node = head
        while (l1 is not None) or (l2 is not None):
            # Handle one list is end alreay case
            if l1 is None:
                current_node.next = l2
                l2 = l2.next
            elif l2 is None:
                current_node.next = l1
                l1 = l1.next
            else:
            # Normal case
                if l1.val >= l2.val:
                    current_node.next = l2
                    l2 = l2.next
                else:
                    current_node.next = l1
                    l1 = l1.next
            current_node = current_node.next
            
        return head

