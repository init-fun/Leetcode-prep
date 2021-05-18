# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, first: ListNode, second: ListNode) -> ListNode:
        
        dummy = ListNode(0)
        very_first = dummy
        while first and second:
            if first.val <= second.val:
                dummy.next = ListNode(first.val)
                first = first.next
            else:
                dummy.next = ListNode(second.val)
                second = second.next
            dummy = dummy.next
            
        while first:
            dummy.next = ListNode(first.val)
            first =first.next
            dummy = dummy.next
            
        while second:
            dummy.next = ListNode(second.val)
            second = second.next
            dummy = dummy.next
            
        return very_first.next
        
        
        
        