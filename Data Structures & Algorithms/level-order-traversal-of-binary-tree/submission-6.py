# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = collections.deque([root])
        res = [[root.val]]
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    if node.left:
                        level.append(node.left.val)
                    if node.right:
                        level.append(node.right.val)
                    q.extend([node.left, node.right])
                
            if level:
                res.append(level)

        return res