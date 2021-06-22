# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cnode = head
        
        while cnode:
            if cnode.next and cnode.next.val == cnode.val:
                cnode.next = cnode.next.next
            else:
                cnode = cnode.next
        return head