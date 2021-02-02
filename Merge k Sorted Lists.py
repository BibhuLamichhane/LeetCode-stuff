# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        try:
            final = []
            for lst in lists:
                curr = lst
                while curr is not None:
                    final.append(curr.val)
                    curr = curr.next
            final.sort()
            head = ListNode(final[0])
            curr = head
            for i in range(1, len(final)):
                new_node = ListNode(final[i])
                curr.next = new_node
                curr = curr.next

            return head
        except:
            return ListNode(val='')
