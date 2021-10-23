# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        vals = set()
        curr = head
        while curr is not None:
            vals.add(curr.val)
            curr = curr.next
        
        vals = list(vals)
        print(vals)
        if len(vals) == 0:
            return head
        vals.sort()
        new_head = ListNode(vals[0])
        curr = new_head
        for i in range(1, len(vals)):
            new_node = ListNode(vals[i])
            curr.next = new_node
            curr = curr.next
        return new_head