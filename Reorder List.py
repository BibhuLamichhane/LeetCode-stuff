# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        val = []
        curr = head
        while curr is not None:
            val.append(curr.val)
            curr = curr.next
            
        n = len(val) - 1
        b = []
        
        for i in range(n//2 + 1):
            b.append(val[i])
            b.append(val[n - i])
        if len(val) % 2:
            b.pop()
        curr = head
        for i in b:
            curr.val = i
            curr = curr.next