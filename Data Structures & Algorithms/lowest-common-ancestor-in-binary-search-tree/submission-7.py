# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return

        if root.left and root.right:
            if p.val < root.val and q.val < root.val:
                root = self.lowestCommonAncestor(root.left, p, q)
            elif p.val > root.val and q.val > root.val:
                root = self.lowestCommonAncestor(root.right, p, q)
            else:
                return root

        
        # return root when both have reached a common ancestor

        return root