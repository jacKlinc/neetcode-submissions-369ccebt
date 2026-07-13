# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # recursive base case
        if not root1 and not root2:
            return None

        value1 = root1.val if root1 else 0 
        value2 = root2.val if root2 else 0 
        # add root1.val and root2.val

        new_root = TreeNode(value1 + value2)
        new_root.left = self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
        new_root.right = self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)

        return new_root