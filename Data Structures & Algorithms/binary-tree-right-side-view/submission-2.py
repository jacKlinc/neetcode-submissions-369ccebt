# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
       # if not root:
        #    return
        # Works for case
        """
        self.res = [root.val]
        
        def dfs(curr):
            if not curr.right:
                return 
            self.res.append(curr.right.val)
            curr = curr.right
            dfs(curr)"""

        """def dfs(curr):
            # Needs to append all values in call level
            # Appends the right-most values
            if not curr:
                return
            if curr.right:
                self.res.append(curr.right.val)
                curr = curr.right
            # if there is no right value, use left
            elif curr.left: 
                self.res.append(curr.left.val)
                curr = curr.left
            else:
                return
            
            dfs(curr)

        dfs(root)

        """
        # best to use BFS for this. in a tree: AKA Level Order Traversal
        q = collections.deque([root])
        res = []
        while q:
            right = None
            q_len = len(q)
            for _ in range(q_len):
                node = q.popleft()
                if node: 
                    right = node
                    q.append(node.left)
                    q.append(node.right)
            if right:
                res.append(right.val)
            
        return res
