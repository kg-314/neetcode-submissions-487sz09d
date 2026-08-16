# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        newNum = node = ListNode()
        carry = 0
        
        while l1 and l2:
            sum = l1.val + l2.val + carry
            if sum >= 10:
                carry = 1
                node.next = ListNode(sum % 10)
            else:
                carry = 0
                node.next = ListNode(sum)
            node = node.next
            l1 = l1.next
            l2 = l2.next
        
        if l1:
            node.next = l1
        if l2:
            node.next = l2
        while carry:
            if not node.next:
                node.next = ListNode(1)
                carry = 0
            elif (node.next.val + 1) >= 10:
                carry = 1
                node.next.val = 0
            else:
                carry = 0
                node.next.val += 1
            node = node.next
        return newNum.next
            