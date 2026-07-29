class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        visited = set()

        def dfs(r: int, c: int):
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
                        and grid[i][j] == "1"
                        and (i, j) not in visited
                    ):
                        visited.add((i, j))
                        q.append((i, j))

        for r in range(rows := len(grid)):
            for c in range(cols := len(grid[0])):
                if (r, c) not in visited and grid[r][c] == "1":
                    dfs(r, c)
                    cnt += 1

        return cnt
