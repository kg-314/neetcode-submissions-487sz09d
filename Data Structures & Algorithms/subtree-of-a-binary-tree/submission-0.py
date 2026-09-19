# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        queue = deque()

        queue.append(root)

        while queue:
            node = queue.popleft()

            if node:
                queue.append(node.left)
                queue.append(node.right)

                if node.val == subRoot.val:
                    if self.checkSame(node, subRoot):
                        return True
        return False
    
    def checkSame(self, root, subRoot):
        stack1 = []
        stack2 = []

        stack1.append(root)
        stack2.append(subRoot)

        while stack1 and stack2:
            node1 = stack1.pop()
            node2 = stack2.pop()

            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val != node2.val:
                return False
            
            
            stack1.append(node1.right)
            
            stack1.append(node1.left)
            
            stack2.append(node2.right)
            
            stack2.append(node2.left)
        if stack1 or stack2:
            return False
        return True

        