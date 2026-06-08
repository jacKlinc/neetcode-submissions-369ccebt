# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.diameter = 0

        # returns the height
        def dfs(curr):
            # null node
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)

            self.diameter = max(self.diameter, right + left)
            
            # 1 is added to count the last edge to the root
            return 1 + max(left, right)

        dfs(root)

        return self.diameter