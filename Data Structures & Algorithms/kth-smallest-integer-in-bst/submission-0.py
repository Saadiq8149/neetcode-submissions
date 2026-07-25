class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.res = None

        def traverse(tree):
            if not tree or self.res is not None:
                return
            
            traverse(tree.left)
            
            if self.res is None:
                self.k -= 1
                if self.k == 0:
                    self.res = tree.val
                    return
            
            traverse(tree.right)

        traverse(root)
        return self.res