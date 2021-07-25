class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # left node right
        global vals
        vals = []
        self.traverse(root)
        return vals
        
    def traverse(self, root):
        global vals
        
        if root is not None:
            if root.left is not None:
                self.traverse(root.left)

            vals.append(root.val)

            if root.right is not None:
                self.traverse(root.right)