# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len = 0

        node = head
        while node:
            len += 1
            node = node.next
        
        nodeToRemove = len - n

        if nodeToRemove == 0:
            return head.next

        node = head
        prev = None

        for i in range(0, nodeToRemove):
            prev = node
            node = node.next
        prev.next = node.next
        node.next = None
        return head