# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #         q = deque()

        #         dummy = ListNode(0)
        #         dummy.next = head

        #         cnode = dummy.next

        #         while cnode:
        #             q.append(cnode)
        #             cnode = cnode.next

        #         # we got our queue

        #         cur = dummy
        #         even = False
        #         while q:
        #             node = q.pop() if even else q.popleft()
        #             node.next = None
        #             # we got the popped node
        #             cur.next = node
        #             cur = cur.next
        #             if even:
        #                 even = False
        #             else:
        #                 even = True
        #         return head

        # divide the list and find the middle node
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # middle node is at slow

        # now reversing the second half of the list
        prev_node = None
        while slow.next:
            next_node = slow.next
            slow.next = prev_node
            prev_node = slow
            slow = next_node

        # our prev_node is the first node of the reverse list

        dummy = ListNode(0)
        very_first = dummy.next

        first = head
        second = prev_node

        while first and second:
            dummy.next = ListNode(first.val)
            dummy = dummy.next
            dummy.next = ListNode(second.val)
            dummy = dummy.next
            first = first.next
            second = second.next

        while first:
            dummy.next = ListNode(first.val)
            first = first.next

        while second:
            dummy.next = ListNode(second.val)
            second = second.next

        return very_first