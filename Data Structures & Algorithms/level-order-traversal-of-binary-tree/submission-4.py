# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def dfs(curr, level):
            if not curr:
                return

            if len(res)-1 < level:
                res.append([])

            res[level].append(curr.val)
            dfs(curr.left, level+1)
            dfs(curr.right, level+1)

        dfs(root, 0)
        return res