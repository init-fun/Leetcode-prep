# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
#         if head is None:
#             return False
#         sptr = head
#         fptr = head
#         while fptr and fptr.next:
#             sptr = sptr.next
#             fptr = fptr.next.next
            
#             if sptr == fptr:
#                 return True
        
#         return False
        
        if head is None:
            return False
        
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
    
            