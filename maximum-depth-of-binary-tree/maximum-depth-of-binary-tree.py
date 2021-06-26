# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        q = deque()
        q.append(root)
        dp = 0
        while len(q):
            dp += 1
            level_len = len(q)
            level_nodes = []
            for i in range(level_len):
                ele = q.popleft()
                if ele.left:
                    q.append(ele.left)
                if ele.right:
                    q.append(ele.right)
        return dp
                