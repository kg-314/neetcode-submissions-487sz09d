# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        root = head
        prev = root
        
        if root.next:
            root = root.next
        else:
            return head
        prev.next = None


        while root.next:
            temp = root.next
            root.next = prev
            prev = root
            root = temp
        
        root.next = prev

        return root