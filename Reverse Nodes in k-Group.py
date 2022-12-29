class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        vals = []
        curr = head
        while curr is not None:
            vals.append(curr.val)
            curr = curr.next
        
        for i in range(0, len(vals), k):
            if len(vals[i:i+k]) == k:
                vals[i:i+k] = vals[i:i+k][::-1]
        
        h = ListNode(vals[0])
        curr = h
        for i in vals[1:]:
            new_node = ListNode(i)
            curr.next = new_node
            curr = curr.next
        return h