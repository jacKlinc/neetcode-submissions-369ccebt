class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # pacific = [0][0:end], [0:end][0]
        # atlantic = [end][0:end], [end][0:end]

        # Optimal Solution O(n * m): start at atlantic/pacific and work inwards
        # the intersecting cells of the two solutions are the result
        pac, atl = set(), set()
        rows, cols = len(heights), len(heights[0])

        def dfs(r: int, c: int, visited: Set, prev: int):
            if (
                (r, c) in visited
                or r not in range(rows)
                or c not in range(cols)
                or heights[r][c] < prev
            ):
                return

            visited.add((r, c))
            for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                dfs(r + dr, c + dc, visited, heights[r][c])

        # loop the top row (atlantic)
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])

        for r in range(rows):
            # loop the first row (pacific)
            # loop the bottom row (atlantic)
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res
