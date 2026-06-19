# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # tortiose and hare algorithm
        if not head:
            return False

        # could loop until the end and 
        # how do we know its the end?
        # could store nodes in list
        new_head = head
        node_lookup = set() # key is index, val is Node.val
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
            
            
        return False