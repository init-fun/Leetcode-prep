# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        is_sorted = self._inorder(root, result=[])
        for i in range(1, len(is_sorted)):
            if is_sorted[i-1] >= is_sorted[i]:
                return False
        return True
    
    def _inorder(self, cnode, result = []):
        if cnode:
            result = self._inorder(cnode.left, result)
            result.append(cnode.val)
            result = self._inorder(cnode.right, result)
        return result
            