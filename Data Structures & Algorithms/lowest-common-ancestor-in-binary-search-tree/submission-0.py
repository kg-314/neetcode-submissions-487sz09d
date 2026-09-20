# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        seen = set()
        seen.add(root)
        self.ans = None

        # have dfs return a boolean if this path is correct
        def firstDFS(root, wanted):
            if root and root.val == wanted.val:
                seen.add(root)
                return True

            if root and firstDFS(root.left, wanted):
                seen.add(root.left)
                return True
            if root and firstDFS(root.right, wanted):
                seen.add(root.right)
                return True
            
            return False

        firstDFS(root, p)

        def secondDFS(root, wanted):
            if root and root.val == wanted.val:
                if root in seen:
                    self.ans = root
                return True
            
            if root and secondDFS(root.left, wanted):
                if self.ans is None:
                    if root in seen:
                        self.ans = root
                return True
            if root and secondDFS(root.right, wanted):
                if self.ans is None:
                    if root in seen:
                        self.ans = root
                return True
            return False

        secondDFS(root, q)

        return self.ans
