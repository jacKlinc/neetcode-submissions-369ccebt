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

        def dfs(node):
            if node in old_new:
                # returns new node
                return old_new[node]

            clone = Node(node.val)
            # map old to new
            old_new[node] = clone
            # run dfs on all neighbors
            clone.neighbors = [dfs(n) for n in node.neighbors]

            return clone

        return dfs(node)
