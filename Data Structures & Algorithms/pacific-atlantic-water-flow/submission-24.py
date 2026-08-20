class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()
        ROWS, COLS = range(R := len(heights)), range(C := len(heights[0]))

        def dfs(r, c, visited, prev):
            if r not in ROWS or c not in COLS or (r, c) in visited or heights[r][c] < prev:
                return

            visited.add((r, c))
            for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                dfs(r + dr, c + dc, visited, heights[r][c])

        for r in ROWS:
            dfs(r, 0, pac, heights[r][0])
            dfs(r, C - 1, atl, heights[r][C - 1])

        for c in COLS:
            dfs(0, c, pac, heights[0][c])
            dfs(R - 1, c, atl, heights[R - 1][c])

        return [[r, c] for r in ROWS for c in COLS if (r, c) in atl and (r, c) in pac]
