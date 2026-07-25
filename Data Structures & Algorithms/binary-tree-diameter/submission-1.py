class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxD = 0

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            self.maxD = max(self.maxD, left + right)

            return 1 + max(left, right)

        dfs(root)
        return self.maxD
