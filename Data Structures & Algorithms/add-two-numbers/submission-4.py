# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0

        curr1 = l1
        curr2 = l2

        while curr1 and curr2:
            s = curr1.val + curr2.val + carry
            curr1.val = s % 10
            curr2.val = s % 10
            carry = s // 10

            curr1 = curr1.next
            curr2 = curr2.next

        if curr1:
            while carry and curr1:
                s = curr1.val + carry
                curr1.val = s % 10
                carry = s // 10
                curr1 = curr1.next
            if carry:
                curr1 = l1
                while curr1.next:
                    curr1 = curr1.next
                curr1.next = ListNode(carry)
            return l1
        elif curr2:
            while carry and curr2:
                s = curr2.val + carry
                curr2.val = s % 10
                carry = s // 10
                curr2 = curr2.next
            if carry:
                curr2 = l2
                while curr2.next:
                    curr2 = curr2.next
                curr2.next = ListNode(carry)
            return l2
        else:
            if carry:
                curr2 = l2
                while curr2.next:
                    curr2 = curr2.next
                curr2.next = ListNode(carry)
            return l2

