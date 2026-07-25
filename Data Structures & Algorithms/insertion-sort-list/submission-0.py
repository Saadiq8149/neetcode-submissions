# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = head

        while curr1:
            curr2 = curr1.next
            while curr2:
                if curr2.val < curr1.val:
                    curr1.val, curr2.val = curr2.val, curr1.val
                curr2 = curr2.next
            curr1 = curr1.next

        return head