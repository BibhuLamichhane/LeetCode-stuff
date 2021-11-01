# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        curr = head
        vals = []
        while curr is not None:
            if curr.val != val:
                vals.append(curr.val)
            curr = curr.next
        try:
            n_head = ListNode(vals[0])
        except:
            return None
        prev = n_head
        vals.pop(0)
        for v in vals:
            new_node = ListNode(v)
            prev.next = new_node
            prev = prev.next
        return n_head