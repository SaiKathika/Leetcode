#Create a separate list as result, move nodes from original list to the result list.
#Only scan from the beginning if p.val, the previous value of the last inserted one, 
# is larger than the next one to be inserted.
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        p = dummy = ListNode()
        while head:
            if p.val > head.val:
                p = dummy
            while p.next and p.next.val < head.val:
                p = p.next
            p.next, head.next, head = head, p.next, head.next
        return dummy.next