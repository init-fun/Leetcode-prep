# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev_node = None
        cnode = head
        
        while cnode:
            next_node = cnode.next
            cnode.next = prev_node
            prev_node = cnode
            cnode = next_node
        
        return prev_node