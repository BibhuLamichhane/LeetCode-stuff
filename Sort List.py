# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        curr = head
        val = []
        while curr is not None:
            val.append(curr.val)
            curr = curr.next

        val.sort()
        
        curr = head
        for v in val:
            curr.val = v
            curr = curr.next
        
        return head