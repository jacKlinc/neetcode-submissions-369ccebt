class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r, c))

            while q:
                row, col = q.popleft()
                for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    i, j = row + dr, col + dc
                    if (
                        i in range(ROWS)
                        and j in range(COLS)
                        and (i, j) not in visited
                        and grid[i][j] == "1"
                    ):
                        q.append((i, j))
                        visited.add((i, j))

        cnt = 0
        for r in range(ROWS := len(grid)):
            for c in range(COLS := len(grid[0])):
                if (r, c) not in visited and grid[r][c] == "1":
                    bfs(r, c)
                    cnt += 1

        return cnt
