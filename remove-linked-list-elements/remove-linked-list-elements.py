# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy_head = ListNode(0)
        dummy_head.next = head
        
        cnode = dummy_head
        
        while cnode.next:
            if cnode.next.val == val:
                cnode.next = cnode.next.next
            else:
                cnode = cnode.next
            
        return dummy_head.next
            
            