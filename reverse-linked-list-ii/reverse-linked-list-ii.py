# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
#         handle base cases
        if left == right:
            return head
        
        current_node = head
        pre_left_node = None
        post_right_node = None
        idx = 1
        while current_node is not None:
#             Default next node
            next_node = current_node.next
#             Save left - 1 node for further head assigning
            if idx == (left - 1):
                next_node = current_node.next
                pre_left_node = current_node
                
#           Start to iter and reverse list from here until right
            elif idx == left:
                next_node = current_node.next
                left_node = current_node
                previous_node = current_node
                
#             Itering until reach right
            elif (left < idx) and (idx < right):
                next_node = current_node.next
                current_node.next = previous_node
                previous_node = current_node
            
#                 Do head reassigning
            elif idx == right:
                post_right_node = current_node.next
                current_node.next = previous_node
#                 re assign heads
                if pre_left_node is None:
                    head = current_node
                else:
                    pre_left_node.next = current_node
                left_node.next = post_right_node
                break
            
            current_node = next_node
            idx += 1
            
            
        return head
                
                
        