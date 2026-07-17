# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # sounds more like a BFS with a heap?
        # heap can be used to find nsmallest
        # or could DFS to update an iterable
        # return nsmallest (get needs to be O(1) to satisfy O(n))
        

        # Solution seems to do DFS iteratively
        if not root:
            return 0
        n = 0 # when n == k, return n
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val

            curr = curr.right

        

