"""
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return

        # map old to new values
        old_new = {}
        # for: 1 -> 2 -> 3
        # clone 1 in map
        # clone 2 in map, save 1, 3 as neighbor
        # use Node 3 (already exists) in map, save 2 as neighbor but it already exists no need to create a new Node

        def dfs(node):
            if node in old_new:
                return old_new[node]

            clone = Node(node.val)
            # map old node to the clone
            old_new[node] = clone
            # copy each neighbor to clone
            clone.neighbors = [dfs(n) for n in node.neighbors]

            return clone

        return dfs(node)
