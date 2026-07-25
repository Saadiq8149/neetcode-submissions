# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(curr, maxVal):
            if not curr:
                return 0

            res = 1 if curr.val >= maxVal else 0
            res += dfs(curr.left, max(maxVal, curr.val))
            res += dfs(curr.right, max(maxVal, curr.val))

            return res

        return dfs(root, root.val)