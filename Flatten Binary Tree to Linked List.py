
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node):
        # root left right
        global vals
        
        vals.append(node.val)
        
        if node.left is not None:
            self.traverse(node.left)
        
        if node.right is not None:
            self.traverse(node.right)
    
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        global vals
        vals = []
        if root is None:
            return
        self.traverse(root)
        print(vals)
        curr = root
        curr.val = vals[0]
        curr.left = None
        print(curr.val)
        for i in vals[1:]:
            new_node = TreeNode(val=i)
            curr.right = new_node
            curr = curr.right
