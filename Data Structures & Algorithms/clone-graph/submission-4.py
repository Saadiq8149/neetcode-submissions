"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        old_to_new = {}

        def dfs(root):
            if not root:
                return

            new = Node(root.val)
            old_to_new[root] = new 
            for n in root.neighbors:
                if n in old_to_new:
                    new.neighbors.append(old_to_new[n])
                else:
                    new.neighbors.append(dfs(n))

            return new

        return dfs(node)