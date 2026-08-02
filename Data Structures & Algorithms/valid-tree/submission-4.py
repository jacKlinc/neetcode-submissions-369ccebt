class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_l = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj_l[n1].append(n2)
            adj_l[n2].append(n1)

        visited = set()

        def dfs(cur, prev):
            if cur in visited:
                return False
            visited.add(cur)
            for neighbour in adj_l[cur]:
                if neighbour == prev:
                    continue
                if not dfs(neighbour,cur):
                    return False

            return True

        return dfs(0, -1) and len(visited) == n
