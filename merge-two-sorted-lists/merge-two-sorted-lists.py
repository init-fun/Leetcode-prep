# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_list = ListNode()
        very_first_node = new_list
        
        while l1 and l2:
            if l1.val <= l2.val:
                new_list.next = ListNode(l1.val)
                new_list = new_list.next
                l1 = l1.next
            else:
                new_list.next = ListNode(l2.val)
                new_list = new_list.next
                l2 = l2.next
        
        while l1:
                new_list.next = ListNode(l1.val)
                new_list = new_list.next
                l1 = l1.next
            
        while l2:
                new_list.next = ListNode(l2.val)
                new_list = new_list.next
                l2 = l2.next
        
        return very_first_node.next
        
        
        