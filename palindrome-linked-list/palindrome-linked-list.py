# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # first go to the middle point of the lst
        # and then reverse the list and checkout whether they are equal or not
        
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow is the first node of the second half
        
        prev_node = None
        while slow:
            next_node = slow.next
            slow.next = prev_node
            prev_node = slow
            slow = next_node
        
        # prev_node is the first node of the second half
        while prev_node:
            if prev_node.val != head.val:
                return False
            prev_node = prev_node.next
            head = head.next
        return True
        
        
        
        
        
        
        
        
        
        
        
        
        