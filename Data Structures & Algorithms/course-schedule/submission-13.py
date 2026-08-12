class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_l = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adj_l[crs].append(pre)

        visited = set()

        def dfs(node):
            if node in visited:
                return False
            if not adj_l[node]:
                return True

            visited.add(node)
            for neighbour in adj_l[node]:
                if not dfs(neighbour):
                    return False

            adj_l[node] = []
            visited.remove(node)
            
            return True

        for n in range(numCourses):
            if not dfs(n):
                return False

        return True
