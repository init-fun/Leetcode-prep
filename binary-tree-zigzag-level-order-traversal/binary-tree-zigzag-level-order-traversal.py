# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        q.append(root)
        res = []
        lvl_count = -1
        while q:
            levelsize = len(q)
            levelnodes = []
            lvl_count += 1
            for _ in range(levelsize):
                ele = q.popleft()
                if ele:
                    levelnodes.append(ele.val)
                    if ele.left:
                        q.append(ele.left)
                    if ele.right:
                        q.append(ele.right)
            if lvl_count % 2 != 0:
                # reverse order
                levelnodes = levelnodes[::-1]
            res.append(levelnodes)
        return res
        