# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode()
        first_node= res
        while l1 and l2:
            if l1.val <= l2.val:
                res.next = ListNode(l1.val)
                l1 = l1.next
                res = res.next
            elif l1.val >= l2.val:
                res.next =  ListNode(l2.val)
                l2 = l2.next
                res = res.next

        
        while l1:
            res.next = ListNode(l1.val)
            l1 = l1.next
            res = res.next
        
        while l2:
            res.next = ListNode(l2.val)
            l2 = l2.next
            res = res.next
        
        return first_node.next