# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue1 = deque()
        queue2 = deque()

        queue1.append(p)
        queue2.append(q)

        if not p and not q:
            return True
        if not p and q:
            return False
        if p and not q:
            return False

        while queue1 and queue2:
            node1 = queue1.popleft()
            node2 = queue2.popleft()

            if node1 and node2:
                if node1.val != node2.val:
                    return False
                queue1.append(node1.left)
                queue1.append(node1.right)

                queue2.append(node2.left)
                queue2.append(node2.right)
            elif node1 and not node2:
                return False
            elif not node1 and  node2:
                return False
            
        
        if queue1 or queue2:
            return False
        return True
