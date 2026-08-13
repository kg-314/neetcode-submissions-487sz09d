# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # optimal (in place)
        if not head:
            return

        # find middle
        fast = head.next
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        

        node = slow.next
        slow.next = None
        prev = None

        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        
        curr = head
        node = prev
        while node:
            temp = curr.next
            curr.next = node
            node = node.next
            curr.next.next = temp
            curr = temp