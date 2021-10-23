class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        curr = head
        val = []
        while curr is not None:
            val.append(curr.val)
            curr = curr.next
        
        for i in range(1, len(val)):
            itbi = val[i]
            curr_val = i - 1
            while (val[curr_val] > itbi) and (curr_val > -1):
                val[curr_val + 1] = val[curr_val]
                curr_val -= 1
            val[curr_val + 1] = itbi
        
        curr = head
        for v in val:
            curr.val = v
            curr = curr.next
        
        return head