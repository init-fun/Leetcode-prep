class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, data=None):
        self.head = Node(data)

    def inset_at_begining(self, ele):
        if self.head is None:
            self.head = Node(ele)
            return
        cnode = self.head
        new_node = Node(ele)
        new_node.next = cnode
        self.head = new_node
        return

    def display(self):
        if self.head is None:
            print("Empty list")
            return
        cnode = self.head
        while cnode:
            print(f"{cnode.data}", end=" > ")
            cnode = cnode.next
        print()
        return


def has_cycle(head):
    if head is None:
        return False
    slow = head
    fast = head
    fix_pos = 0
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        fix_pos += 1
        if fast == slow:
            mark = fast
            break
    count = 1
    slow = slow.next
    while slow != mark:
        slow = slow.next
        count += 1
    return count


def first_node_of_cycle(head):
    slow, fast = head, head

    while fast and fast.next:  # O(n)
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            cycle_mark = slow
            break
    else:
        return False

    count = 1
    slow = slow.next

    while slow != cycle_mark:  # O(n)
        slow = slow.next
        count += 1
    # count has cyclic len
    start = 0
    cnode = head
    while start != count:
        cnode = cnode.next
        start += 1

    new_head = head
    while new_head != cnode:
        new_head = new_head.next
        cnode = cnode.next
        if cnode == new_head:
            return cnode

    return False
