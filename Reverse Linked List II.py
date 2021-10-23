# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        curr = head
        vals = []
        while curr is not None:
            vals.append(curr.val)
            curr = curr.next
        
        new_vals = vals[:left - 1] + vals[left - 1: right][::-1] + vals[right:]
        
        curr = head
        for i in new_vals:
            curr.val = i
            curr = curr.next
        
        return head