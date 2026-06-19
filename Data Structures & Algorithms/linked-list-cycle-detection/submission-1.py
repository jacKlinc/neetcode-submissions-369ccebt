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
        node_lookup = {} # key is index, val is Node.val
        i = 0
        while new_head.next:
            print(node_lookup)
            # We found it!
            if new_head.val in node_lookup:
                return True
            # Add new entry
            print(new_head.val)
            node_lookup[new_head.val] = i

            # At the end
            if not new_head.next:
                return False
            i += 1
            # assign head to next one
            new_head = new_head.next
            
            
        return False