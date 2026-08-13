# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []

        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        l = 0
        r = len(nodes) - 1

        curr = ListNode()

        while l < r:
            curr.next = nodes[l]
            l += 1
            curr = curr.next

            curr.next = nodes[r]
            r -= 1
            curr = curr.next
        if len(nodes) % 2:
            curr.next = nodes[l]
            curr = curr.next
            curr.next = None
        else:
            curr.next = None


            