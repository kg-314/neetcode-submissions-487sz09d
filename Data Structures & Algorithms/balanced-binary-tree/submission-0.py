# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    balanced = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.checkBal(root)
        return self.balanced

    def checkBal(self, root):
        if not root:
            return 0
        left = self.checkBal(root.left)
        right = self.checkBal(root.right)

        if abs(left - right) > 1:
            self.balanced = False
        
        return 1 + max(left, right)