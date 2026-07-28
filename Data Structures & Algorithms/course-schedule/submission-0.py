class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # this related to topo sort because the traversal order can catch the prereqs
        # b must be taken before a in [a, b]
        # the challenge is to check can we traverse one before the other
        # interpret [a, b] as an edge in a graph

        # the impossible prereqs can be interpreted as a graph cycle
        # a prereq of another means that one must be completed before the other

        # can use an adjacency list as a hash map
        # key: course, value: prerequisites
        # traverse the graph until the end. If a course has valid prereqs, leave the list empty

        pre_req_map = {i: [] for i in range(numCourses)}  # crs: pre_req
        for crs, pre in prerequisites:
            pre_req_map[crs].append(pre)

        visited = set()

        def dfs(crs: int):
            if crs in visited:
                return False
            # course has not prerequisites
            if pre_req_map[crs] == []:
                return True

            visited.add(crs)
            for pre in pre_req_map[crs]:
                # finds courses that can't be completed
                if not dfs(pre):
                    return False
            # we know the course can be taken
            visited.remove(crs)
            # This will return True immediately earlier in the function
            pre_req_map[crs] = []

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
