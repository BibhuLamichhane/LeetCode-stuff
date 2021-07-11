class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        vals = []
        curr = head
        while curr is not None:
            vals.append(curr.val)
            curr = curr.next
            
        l = len(vals)
        if l < 2:
            pass
        else:
            k = k % l
            print(k)
            for i in range(k):
                vals.insert(0, vals[-1])
                vals.pop()

            curr = head
            for i in vals:
                curr.val = i
                curr = curr.next
        return head