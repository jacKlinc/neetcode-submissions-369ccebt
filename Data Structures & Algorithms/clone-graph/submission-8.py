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

        def dfs(cur):
            if cur in old_new:
                return old_new[cur]

            clone = Node(cur.val)
            old_new[cur] = clone
            clone.neighbors = [dfs(n) for n in cur.neighbors]

            return clone

        return dfs(node)
