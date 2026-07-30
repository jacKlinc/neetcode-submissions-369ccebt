class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # there is a forest of trees where each node is a tree
        # each iteration connects current and previous node
        # each connection decrements the n (5)
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(node):
            res = node

            while res != parent[res]:
                # optimisation: set to grandparent
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res

        def union(node1, node2):
            # find root parents of each
            parent1, parent2 = find(node1), find(node2)

            # 0 indicates no union
            if parent1 == parent2:
                return 0

            # if the rank is higher, it means it is the parent
            if rank[parent2] > rank[parent1]:
                parent[parent1] = parent2
                rank[parent2] += rank[parent1]
            else:
                parent[parent2] = parent1
                rank[parent1] += rank[parent2]

            return 1  # successful union

        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)

        return res
