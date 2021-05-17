# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, data: int) -> ListNode:
        dummy_head = ListNode(-1)
        dummy_head.next = head
        
        cnode= dummy_head
        while cnode.next: # this is the first element of our linkedlist
            if cnode.next.val == data:
                cnode.next = cnode.next.next
            else:
                cnode =cnode.next
        return dummy_head.next
                
        