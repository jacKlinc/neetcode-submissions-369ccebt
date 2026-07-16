# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # the root is always good because no nodes above can be bigger
        # nodes equal are also good
        # siblings don't matter, we care about ancestors
        self.good = 0

        def dfs(node, max_val):
            if not node:
                return

            if node.val >= max_val:
                self.good += 1

            max_val = max(node.val, max_val)

            dfs(node.left, max_val)
            dfs(node.right, max_val)

        dfs(root, root.val)

        return self.good
