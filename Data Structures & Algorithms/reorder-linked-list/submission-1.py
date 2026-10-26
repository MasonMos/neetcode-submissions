# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        half = head
        otherHalf = head

        def reverse(head):
            start = head
            prev = None

            while start is not None:
                temp = start.next
                start.next = prev
                prev = start
                start = temp

            return prev
        
        while otherHalf and otherHalf.next is not None:
            half = half.next
            otherHalf = otherHalf.next.next
        
        reversed = reverse(half.next)
        half.next = None

        curr = head
        revCurr = reversed

        while revCurr:
            currTemp = curr.next
            revTemp = revCurr.next
            curr.next = revCurr
            revCurr.next = currTemp
            curr = currTemp
            revCurr = revTemp
        





