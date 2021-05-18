# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        q = deque()
        
        dummy = ListNode(0)
        dummy.next = head
        
        cnode = dummy.next
        
        while cnode:
            q.append(cnode)
            cnode = cnode.next
        
        # we got our queue
        
        cur = dummy
        even = False
        while q:
            node = q.pop() if even else q.popleft()
            node.next = None
            # we got the popped node
            cur.next = node
            cur = cur.next
            if even:
                even = False
            else:
                even = True
        return head
            