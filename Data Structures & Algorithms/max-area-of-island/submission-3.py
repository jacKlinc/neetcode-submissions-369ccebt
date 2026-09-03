class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # the edge is water
        # The example actually has three islands but we want the biggest one
        ROWS, COLS = len(grid), len(grid[0])
        parents = list(range(n := ROWS * COLS))
        rank = [1] * n

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False

            if rank[px] > rank[py]:
                rank[px] += rank[py]
                parents[py] = x
            else:
                rank[py] += rank[px]
                parents[px] = y

            return False

        max_area = 0
        index = lambda r, c: r * COLS + c
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    continue
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    i, j = r + dr, c + dc
                    if i not in range(ROWS) or j not in range(COLS) or grid[i][j] == 0:
                        continue
                    union(index(r, c), index(i, j))

                area = rank[find(index(r, c))]
                max_area = max(max_area, area)

        return max_area
