# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, root, k):
        prev, curr = None, root

        for _ in range(k):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0

        curr = head
        while curr:
            curr = curr.next
            length += 1

        dummy = ListNode()
        dummy.next = head
        
        curr = head
        prev = dummy

        for _ in range(length // k):
            temp = curr
            for _ in range(k):
                temp = temp.next
            
            rev = self.reverse(curr, k)
            
            prev.next = rev
            for _ in range(k-1):
                rev = rev.next
            rev.next = temp

            prev = rev
            curr = temp

        return dummy.next