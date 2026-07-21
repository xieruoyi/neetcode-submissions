class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root

        if root.left and root.right:
            dummy = root.left
            root.left = root.right
            root.right = dummy

        elif root.left and root.right == None:
            root.right = root.left
            root.left = None

        elif root.right and root.left == None:
            root.left = root.right
            root.right = None

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root