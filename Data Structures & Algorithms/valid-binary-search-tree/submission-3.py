class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.valid = True

        def dfs(tree, minVal, maxVal):
            if not tree:
                return

            if not (minVal < tree.val < maxVal):
                self.valid = False
                return

            dfs(tree.left, minVal, tree.val)
            dfs(tree.right, tree.val, maxVal)

        dfs(root, float('-inf'), float('inf'))
        return self.valid