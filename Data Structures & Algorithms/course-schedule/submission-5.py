class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_l = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adj_l[crs].append(pre)

        visited = set()

        def dfs(n):
            if n in visited:
                return False
            if not adj_l[n]:
                return True

            visited.add(n)
            for pre in adj_l[n]:
                if not dfs(pre):
                    return False

            visited.remove(n)
            adj_l[n] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
