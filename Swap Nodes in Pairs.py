# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        vals = []
        curr = head
        outlier = 99999999
        while curr is not None:
            vals.append(curr.val)
            curr = curr.next
        if len(vals) < 2:
            return head
        if len(vals) % 2 == 1:
            outlier = vals.pop()
        for i in range(0, len(vals), 2):
            vals[i], vals[i + 1] = vals[i + 1], vals[i]

        if outlier != 99999999:
            vals.append(outlier)
        new_head = ListNode(vals[0])
        curr = new_head
        for i in range(1, len(vals)):
            new_node = ListNode(vals[i])
            curr.next = new_node
            curr = curr.next

        return new_head
