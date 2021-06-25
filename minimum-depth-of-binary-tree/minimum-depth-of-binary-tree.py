# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        depth = 0
        
        q = deque()
        q.append(root)
        while q:
            depth += 1
            level_len = len(q)
    
            for i in range(level_len):
                popped_ele = q.popleft()
                
                if not popped_ele.left and not popped_ele.right:
                    return depth
                
                if popped_ele.left:
                    q.append(popped_ele.left)
                if popped_ele.right:
                    q.append(popped_ele.right)
 
                
                
        
        