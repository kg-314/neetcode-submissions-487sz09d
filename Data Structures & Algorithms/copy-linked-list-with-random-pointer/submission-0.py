"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldNodes = {}

        node = head
        dummy = newNode = Node(0)

        while node:
            newNode.next = Node(node.val)
            oldNodes[node] = newNode.next
            newNode = newNode.next
            node = node.next

        node = head
        newNode = dummy.next
        while node:
            if node.random:
                newNode.random = oldNodes[node.random]
            else:
                newNode.random = None
            node = node.next
            newNode = newNode.next

        return dummy.next
        


