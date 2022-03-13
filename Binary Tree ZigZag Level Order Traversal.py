# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        not_visited = [root]
        o = []
        if root is None:
            return []
        c = 0
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
            if c % 2:
                o[-1] = o[-1][::-1]
                c += 1
            else:
                c += 1
        return o
