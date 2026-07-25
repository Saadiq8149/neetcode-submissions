# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPath = float('-inf')

        def dfs(tree):
            if not tree:
                return 0
            
            left_max = max(dfs(tree.left), 0)
            right_max = max(dfs(tree.right), 0)

            curr_sum = tree.val + left_max + right_max

            self.maxPath = max(curr_sum, self.maxPath)

            return tree.val + max(left_max, right_max)

        dfs(root)
        return self.maxPath
