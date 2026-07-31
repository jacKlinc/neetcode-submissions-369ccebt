class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # use union find algo
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(node):
            x = node
            # found root
            while parent[x] != x:
                parent[x] = find(parent[x])
                x = parent[x]
            return x

        def union(x, y):
            p1, p2 = find(x), find(y)

            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                parent[p2] = p1
            elif rank[p1] < rank[p2]:
                parent[p1] = p2
            else:
                parent[p2] = p1
                rank[p1] += 1
            return True

        res = n
        for u, v in edges:
            if union(u, v):
                res -= 1

        return res
