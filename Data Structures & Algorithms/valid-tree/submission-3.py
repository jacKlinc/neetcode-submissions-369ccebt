class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # create neighbours hash map
        adj_l = {i: [] for i in range(n)}

        visited = set()

        for n1, n2 in edges:
            # each key is a node and the list are its neighbours
            adj_l[n1].append(n2)
            adj_l[n2].append(n1)

        def dfs(node, parent):
            # a validTree has no cycles
            if node in visited:
                return False
            
            visited.add(node)
            for n in adj_l[node]:
                if n == parent:
                    continue
                if not dfs(n, node):
                    return False
            print(visited)

            return True


        return dfs(0, -1) and len(visited)==n
