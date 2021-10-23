# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        global vals
        vals = []
        self.traverse(root)
        return vals
        
    def traverse(self, node):
        global vals
        if node is not None:
            vals.append(node.val)
            
            if node.left is not None:
                self.traverse(node.left)
            
            if node.right is not None:
                self.traverse(node.right)