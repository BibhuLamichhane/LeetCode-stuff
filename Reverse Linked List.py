# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        vals = []
        while curr is not None:
            vals.append(curr.val)
            curr = curr.next
        
        vals = vals[::-1]
        try:
            main = ListNode(vals[0])
        except:
            return None
        curr = main
        for i in vals[1:]:
            new_node = ListNode(i)
            curr.next = new_node
            curr = curr.next
        return main