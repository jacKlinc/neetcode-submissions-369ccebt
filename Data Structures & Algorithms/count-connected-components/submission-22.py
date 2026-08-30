class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Union find: how can we group things by some criteria
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(x):
            # if the parent is not itself: not the root
            if parent[x] != x:
                # go up the parent
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            print(px)
            if px == py:
                return False
            if rank[px] > rank[py]:
                parent[py] = px
                rank[py] += rank[px]
            else:
                parent[px] = py
                rank[px] += rank[py]
            return True

        res = n
        for n1, n2 in edges:
            # if there is no union, no need to update
            if union(n1, n2):
                res -= 1
        return res
