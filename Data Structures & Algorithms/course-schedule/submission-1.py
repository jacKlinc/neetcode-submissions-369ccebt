class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        reqs = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            reqs[crs].append(pre)

        visited = set()

        def dfs(crs):
            # empty list means we found t
            if not reqs[crs]:
                return True
            # cycle detected
            if crs in visited:
                return False

            visited.add(crs)
            # loop over the courses neighbours (prerequisites)
            for pre in reqs[crs]:
                if not dfs(pre):
                    return False

            # course processed
            visited.remove(crs)
            # facilitates early return
            reqs[crs] = []

            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
