class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def ll_to_num(self, linked_list):
        a = linked_list
        num = ''
        while a is not None:
            num += str(a.val)
            a = a.next
        return int(num[::-1])
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = self.ll_to_num(l1)
        num2 = self.ll_to_num(l2)
        num3 = str(num1 + num2)
        num3 = num3[::-1]
        linked_lists = [ListNode(int(i)) for i in num3]
        for i in range(len(linked_lists) - 1):
            linked_lists[i].next = linked_lists[i + 1]
        return linked_lists[0]