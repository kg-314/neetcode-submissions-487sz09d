# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        left = head
        right = head
        cnt = 1
        firstTime = True
        newHead = None
        prev = None

        while right:
            if cnt == k:
                node = None
                tail = left
                
                for i in range(k):
                    temp = left.next
                    left.next = node
                    node = left
                    left = temp
                tail.next = left
                if firstTime:
                    firstTime = False
                    newHead = right
                else:
                    prev.next = right
                prev = tail
                right = left
                cnt = 1
            else:
                right = right.next
                cnt += 1
        return newHead
