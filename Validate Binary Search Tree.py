# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        global vals
        vals = []
        self.traverse(root)
        
        if len(set(vals)) != len(vals):
            return False
        return vals == sorted(vals)
        
    def traverse(self, root):
        global vals
        
        if root is not None:
            if root.left is not None:
                self.traverse(root.left)
            vals.append(root.val)
            if root.right is not None:
                self.traverse(root.right)