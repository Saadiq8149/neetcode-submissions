"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mpp = {None: None}
        
        curr = head

        while curr:
            new = Node(curr.val)
            mpp[curr] = new
            curr = curr.next

        curr = head
        while curr:
            copy = mpp[curr]
            copy.next = mpp[curr.next]
            copy.random = mpp[curr.random]
            curr = curr.next

        return mpp[head]

