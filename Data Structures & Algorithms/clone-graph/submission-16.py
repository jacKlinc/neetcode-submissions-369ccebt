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

        def clone(n):
            if n in old_new:
                return old_new[n]

            new_node = Node(n.val)
            old_new[n] = new_node
            new_node.neighbors = [clone(i) for i in n.neighbors]

            return new_node

        return clone(node)
