# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        v = []
        curr = head
        while curr is not None:
            v.append(curr.val)
            curr = curr.next
            
        prev = ListNode()
        curr = prev
        for i in v:
            if v.count(i) == 1:
                new_node = ListNode(i)
                curr.next = new_node
                curr = curr.next
                
        return prev.next
        
        
