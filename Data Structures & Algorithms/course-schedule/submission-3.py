class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        reqs = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            reqs[crs].append(pre)

        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            if reqs[crs] == []:
                return True

            visited.add(crs)
            for pre in reqs[crs]:
                if not dfs(pre):
                    return False
            
            # After processing one course, clear pre reqs and set
            visited.remove(crs)
            reqs[crs] = []

            return True

        for n in range(numCourses):
            if not dfs(n):
                return False

        return True
