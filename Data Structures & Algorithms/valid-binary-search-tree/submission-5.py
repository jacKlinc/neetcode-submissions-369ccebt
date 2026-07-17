# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # a valid BST is when the left child is less than the parent
        # and the right child is more than the parent
        if not root:
            return True

        q = collections.deque([(root, float("-inf"), float("inf"))])

        while q:
            node, left, right = q.popleft()
            if not left < node.val < right:
                return False
            
            # when moving left, the max value becomes the current node value
            if node.left:
                q.append((node.left, left, node.val))
            
            # when moving right, the min value becomes the current node value
            if node.right:
                q.append((node.right, node.val, right))

        return True
