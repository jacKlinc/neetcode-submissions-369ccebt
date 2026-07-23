class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        # right, left, up, down
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        cnt = 0

        def bfs(r: int, c: int):
            q = deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    i, j = row + dr, col + dc
                    if (
                        i in range(rows)  # in row range
                        and j in range(cols)  # in col range
                        and grid[i][j] == "1"  # is land
                        and (i, j) not in visited  # not visited
                    ):
                        q.append((i, j))
                        visited.add((i, j))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    cnt += 1

        return cnt
