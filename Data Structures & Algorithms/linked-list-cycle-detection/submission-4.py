# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # O(n) time and memory
        if not head:
            return False

        """        # could loop until the end and 
        # how do we know its the end?
        # could store nodes in list
        new_head = head
        node_lookup = set() 
        while new_head.next:
            # We found it!
            if new_head.val in node_lookup:
                return True
            # Add new entry
            node_lookup.add(new_head.val)
            # At the end
            if not new_head.next:
                return False
            # assign head to next one
            new_head = new_head.next
            
        return False"""

        # O(1): tortiose and hare algorithm
        # slow and fast pointers
        # the fast one will find the end of the list and return early
        # the slow one will properly assess otherwise
        # if the pointers meet, that is where the cycle is
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next # shifted by 1
            fast = fast.next.next # shifted by 2
            # found it
            if slow == fast:
                return True

        return False
