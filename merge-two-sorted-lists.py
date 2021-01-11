# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        try:
            vals = []
            l1_curr = l1
            while l1_curr is not None:
                vals.append(l1_curr.val)
                l1_curr = l1_curr.next

            l2_curr = l2
            while l2_curr is not None:
                vals.append(l2_curr.val)
                l2_curr = l2_curr.next

            vals.sort()
            head = ListNode(vals[0])
            curr = head
            for i in range(1, len(vals)):
                new_node = ListNode(vals[i])
                curr.next = new_node
                curr = curr.next
            return head
        except IndexError:
            return l1