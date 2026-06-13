# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # seems like a case for recursion
        if not head:
            return None

        new_head = head
        if head.next:
            new_head = self.reverseList(head.next)
            # reversing link last node to head
            head.next.next = head

        head.next = None

        return new_head