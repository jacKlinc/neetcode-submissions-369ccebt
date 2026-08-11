class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_l = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj_l[n1].append(n2)
            adj_l[n2].append(n1)

        visited = set()

        def dfs(node):
            # if node in visited:
            #     return
            for neighbour in adj_l[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    dfs(neighbour)

        cnt = 0
        for node in range(n):
            if node not in visited:
                dfs(node)
                cnt += 1
        return cnt
