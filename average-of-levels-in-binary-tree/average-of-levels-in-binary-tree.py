# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        q = deque()
        q.append(root)
        res =[]
        while q:
            levelsize = len(q)
            levelnode = []
            for _ in range(levelsize):
                ele = q.popleft()
                levelnode.append(ele.val)
                if ele.left:
                    q.append(ele.left)
                if ele.right:
                    q.append(ele.right)
            res.append(sum(levelnode)/levelsize)
        return res