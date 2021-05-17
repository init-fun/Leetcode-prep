# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from math import ceil
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        count = 0
        cnode = head
        while cnode: # O(n)
            cnode = cnode.next
            count += 1
        # print(count)
        mid_count = count//2
        count = 0
        cnode = head
        while count < mid_count:
            count += 1
            cnode = cnode.next
            
        
        return cnode
        