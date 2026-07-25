# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(curr, minBound, maxBound):
            if not curr:
                return True

            if minBound >= curr.val or maxBound <= curr.val:
                return False

            return dfs(curr.left, minBound, curr.val) and dfs(curr.right, curr.val, maxBound)

        return dfs(root, float('-inf'), float('inf'))
            
            
            

