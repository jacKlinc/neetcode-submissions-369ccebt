class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # start at both pacific and atlantic bounds and work inwards
        # each successive value needs to be less
        # this can be compared using a previous value

        atlantic, pacific = set(), set()
        ROWS, COLS = len(heights), len(heights[0])

        def dfs(r: int, c: int, visited: Set, prev: int):
            if (
                (r, c) in visited
                or r not in range(ROWS)
                or c not in range(COLS)
                or heights[r][c] < prev
            ):
                return

            visited.add((r, c))

            for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                dfs(r + dr, c + dc, visited, heights[r][c])

        # left and right bounds
        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])

        # top and bottom bounds
        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in atlantic and (r, c) in pacific:
                    res.append([r, c])

        return res
