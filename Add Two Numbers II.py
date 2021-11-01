# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = l1
        num1 = ''
        while curr is not None:
            num1 += str(curr.val)
            curr = curr.next
        
        num2 = ''
        curr = l2
        while curr is not None:
            num2 += str(curr.val)
            curr = curr.next
        num = str(int(num1) + int(num2))
        head = ListNode(int(num[0]))
        curr = head
        
        for i in range(1, len(num)):
            new_node = ListNode(num[i])
            curr.next = new_node
            curr = curr.next
        return head