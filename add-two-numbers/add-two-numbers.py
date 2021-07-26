# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1.val == 0 and \
            not l1.next and \
            l2.val == 0 and \
            not l2.next:
            return ListNode(0, None)
        
        return self.sum_(l1, l2, 0)
        
    def sum_(self, node1, node2, surplus):
#         dummy node for more beautiful code
        if node1 is None:
            node1 = ListNode(0, None)
        if node2 is None:
            node2 = ListNode(0, None)

        _sum = node1.val + node2.val + surplus
#         [1,6,0,3,3,6,7,2,0,1], [6,3,0,8,9,6,6,9,6,1] this must bypas when 0+0=0 but there is next
        if _sum == 0 and \
            not node1.next and \
            not node2.next:
            return None
        
        sum_node = ListNode(_sum % 10)
        surplus = _sum // 10
        sum_node.next = self.sum_(node1.next, node2.next, surplus)
        
        return sum_node