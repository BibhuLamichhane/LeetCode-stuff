# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int):
        val_to_remove = self.length(head) - n
        if val_to_remove == 0:
            return head.next
        index = -1
        curr = head
        return_val = []
        if curr.next is None:
            return None
        else:
            while curr.next is not None:
                index += 1
                if index + 1 == val_to_remove:
                    curr.next = curr.next.next
                else:
                    return_val.append(curr)
                    curr = curr.next
            return head

    def length(self, head):
        curr = head
        n = 1
        while curr.next is not None:
            n += 1
            curr = curr.next
        return n 