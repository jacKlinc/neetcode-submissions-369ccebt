class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # could create two adj lists
        # how do I detect that I changed groups?
        # can't just
        adj_l = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj_l[n1].append(n2)
            adj_l[n2].append(n1)

        print(adj_l)
        # could have groups: [[0, 1, 2], [3, 4]]
        # return len(groups)
        # how to populate?
        # Loop over adj list and add to group until value is not there: return sublist
        # or just increment a pointer

        visited = set()

        def dfs(node):
            """This checks for cycles in a connected graph"""
            for neighbour in adj_l[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    dfs(neighbour)

        cnt = 0
        for node in range(n):
            if node not in visited:
                visited.add(node)
                dfs(node)
                cnt += 1

        return cnt
