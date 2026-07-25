class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p, q = p.val, q.val

        def dfs(node):
            if not node:
                return None

            x = node.val

            if x < p and x < q:
                return dfs(node.right)
            elif x > p and x > q:
                return dfs(node.left)
            else:
                return node

        return dfs(root)
