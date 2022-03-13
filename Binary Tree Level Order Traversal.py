# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        not_visited = [root]
        c = 0
        counter = 0
        o = []
        if root is None:
            return []
        
        while not_visited != []:
            o.append([])
            new_branches = []
            for i in not_visited:
                o[-1].append(i.val)
                if i.left is not None:
                    new_branches.append(i.left)
                if i.right is not None:
                    new_branches.append(i.right)
            not_visited = new_branches
        return o
