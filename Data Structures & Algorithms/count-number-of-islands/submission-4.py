class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
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
                        i in range(rows)
                        and j in range(cols)
                        and (i, j) not in visited
                        and grid[i][j] == "1"
                    ):
                        visited.add((i, j))
                        q.append((i, j))

        for r in range(rows := len(grid)):
            for c in range(cols := len(grid[0])):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    cnt += 1

        return cnt
