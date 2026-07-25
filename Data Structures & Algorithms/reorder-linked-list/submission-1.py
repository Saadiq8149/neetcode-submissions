# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = 0

        curr = head

        while curr:
            curr = curr.next
            length += 1

        pivot = length // 2

        head1 = head
        head2 = head

        def reverseLL(root):
            prev, curr = None, root

            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev

        for i in range(pivot):
            head2 = head2.next

        middle = head2.next
        head2.next = None
        head2 = middle
        head2 = reverseLL(head2)

        i = 0
        while head2:
            if i % 2 == 0:
                temp = head1.next 
                head1.next = head2 
                head1 = temp
            else:
                temp = head2.next 
                head2.next = head1 
                head2 = temp
            i += 1



        

        