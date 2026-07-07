# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # for each recursive call it could be incremented
        # this could then be stored in a hashmap
        # Sequence: 0, n-1, 1, n-2, 2, n-3
        # if i % 2 == 0: i /= 2 (unless 0). Index=0, 2, 4, ...
        # else: n - 1. Index=1, 3, 5, ...

        slow, fast = head, head.next

        # check not the end of list
        while fast and fast.next: 
            # Shift each pointer
            slow = slow.next
            fast = fast.next.next # 

        # second half of the list needs to be reversed
        second = slow.next
        slow.next = None
        prev = None
        # reverse second half of list
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge two halves
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

        
        