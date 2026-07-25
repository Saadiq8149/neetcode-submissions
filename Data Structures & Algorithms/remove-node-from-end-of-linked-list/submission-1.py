# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0

        curr = head
        while curr:
            curr = curr.next
            length += 1

        position = length - n
        
        prev = None
        curr = head
        for i in range(position):
            prev = curr
            curr = curr.next

        if not prev:
            if length == 1:
                return None
            return head.next

        prev.next = curr.next
        curr.next = None
        return head