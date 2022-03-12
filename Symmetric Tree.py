# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverse1(self, root):
        global left
        left.append(root.val)
        if root.left is not None:
            self.traverse1(root.left)
        else:
            left.append(None)
        if root.right is not None:
            self.traverse1(root.right) 
        else:
            left.append(None)
    
    def traverse2(self, root):
        global right
        right.append(root.val)
        if root.right is not None:
            self.traverse2(root.right) 
        else:
            right.append(None)
        if root.left is not None:
            self.traverse2(root.left)
        else:
            right.append(None)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        global left, right
        left = []
        right = []
        if root.left is not None:
            self.traverse1(root.left)
        if root.right is not None:
            self.traverse2(root.right)

        return left == right