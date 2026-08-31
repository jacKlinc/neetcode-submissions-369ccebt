class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        n = len(grid) * len(grid[0])
        parents = list(range(n))
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
                parents[py] = px
            else:
                rank[py] += rank[px]
                parents[px] = py

            return True

        index = lambda r, c: r * COLS + c

        islands = 0
        for r in range(ROWS := len(grid)):
            for c in range(COLS := len(grid[0])):
                if grid[r][c] == "1":
                    islands += 1
                    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        i, j = r + dr, c + dc
                        if i not in range(ROWS) or j not in range(COLS) or grid[i][j] == "0":
                            continue
                        if union(index(r, c), index(i, j)):
                            islands -= 1

        return islands
