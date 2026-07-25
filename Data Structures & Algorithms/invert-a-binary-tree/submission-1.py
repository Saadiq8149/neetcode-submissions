# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recurse(root):
            if not root:
                return root
            if not root.left and not root.right:
                return root

            temp = root.left
            root.left = recurse(root.right)
            root.right = recurse(temp)
            return root

        return recurse(root)

            