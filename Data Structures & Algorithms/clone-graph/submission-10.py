"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return

        old_new = {}

        def dfs(root):
            if root in old_new:
                return old_new[root]

            print(old_new)

            clone = Node(root.val)
            old_new[root] = clone
            clone.neighbors = [dfs(n) for n in root.neighbors]

            return clone

        return dfs(node)
