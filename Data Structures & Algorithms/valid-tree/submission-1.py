class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 0:
            return True
        # solution: create adj list and check for cycles

        adj_l = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj_l[n1].append(n2)
            adj_l[n2].append(n1)

        visited = set()

        def dfs(node, prev):
            if node in visited:
                return False
            visited.add(node)
            for n in adj_l[node]:
                # skip if same
                if n == prev:
                    continue

                if not dfs(n, node):
                    # loop
                    return False

            return True
        # start at node, -1 will never exist
        # and the number of visited nodes must match the number of nodes: connected graph
        return dfs(0, -1) and n == len(visited)
