class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # start at edge and work inwards
        ROWS, COLS = len(heights), len(heights[0])
        atl, pac = set(), set()

        def dfs(r, c, visited, prev):
            if (
                r not in range(ROWS)
                or c not in range(COLS)
                or (r, c) in visited
                or heights[r][c] < prev
            ):
                return
            print(r, c, heights[r][c])

            visited.add((r, c))

            for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                dfs(r + dr, c + dc, visited, heights[r][c])

        # top and bottom
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        # left and right
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in atl and (r, c) in pac:
                    res.append([r, c])

        return res
