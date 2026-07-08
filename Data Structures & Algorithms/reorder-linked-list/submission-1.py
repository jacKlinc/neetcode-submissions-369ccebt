# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        # find the middle
        while fast and fast.next:
            # when fast reaches its end, we're at the middle for slow
            slow = slow.next
            fast = fast.next.next # fast basically skips an element on each iteration

        # reverse second half from middle
        second = slow.next
        prev, slow.next = None, None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge halves
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            # stitch the values back together using tmp
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2