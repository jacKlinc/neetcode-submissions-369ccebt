# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        new_head = head 
        # start at the end (null)
        if head.next:
            new_head = self.reverseList(head.next)
            # If this was three elements, this is setting element 3 to element 1
            head.next.next = head

        # Set last element once others are swapped
        head.next = None
        return new_head