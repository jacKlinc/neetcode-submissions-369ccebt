class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_l = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj_l[n1].append(n2)
            adj_l[n2].append(n1)

        visited = set()

        def dfs(node):
            for neighbor in adj_l[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        res = 0
        for node in range(n):
            if node not in visited:
                visited.add(node)
                dfs(node)
                res += 1

        return res
