class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # valid tree: no cycles, must be connected
        visited = set()
        adj_l = {i: [] for i in range(n)}
        # maps the node to its neightbours
        for n1, n2 in edges:
            adj_l[n1].append(n2)
            adj_l[n2].append(n1)

        # when traversing back up the tree, a false positive will be added to the visited set
        # solution: use previous value
        def dfs(i, prev):
            if i in visited:
                return False

            visited.add(i)
            for neightbour in adj_l[i]:
                # skip if the neightbour is the same as before
                if neightbour == prev:
                    continue
                if not dfs(neightbour, i):
                    return False

            return True

        return dfs(0, -1) and n == len(visited)
