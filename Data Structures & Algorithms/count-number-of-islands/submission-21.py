class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Make a list the same number of elements as the grid
        n = len(grid) * len(grid[0])
        parent = list(range(n))
        rank = [1] * n

        # A group in this case is a 1's
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False

            if rank[px] > rank[py]:
                parent[py] = px
                rank[px] += rank[py]
            else:
                parent[px] = py
                rank[py] += rank[px]
            return True

        def index(r, c):
            return r * COLS + c

        cnt = 0
        for r in range(ROWS := len(grid)):
            for c in range(COLS := len(grid[0])):
                if grid[r][c] == "1":
                    cnt += 1
                    for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                        i, j = r + dr, c + dc
                        if i not in range(ROWS) or j not in range(COLS) or grid[i][j] == "0":
                            continue

                        if union(index(r, c), index(i, j)):
                            cnt -= 1

        return cnt
