class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_l = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj_l[n1].append(n2)
            adj_l[n2].append(n1)

        visited = set()

        def dfs(prev, node):
            print(len(visited), visited)
            if node in visited:
                return False

            visited.add(node)
            for neighbour in adj_l[node]:
                if prev == neighbour:
                    continue
               
                if not dfs(node, neighbour):
                    return False
            
            return True

        return dfs(-1, 0) and len(visited) == n
