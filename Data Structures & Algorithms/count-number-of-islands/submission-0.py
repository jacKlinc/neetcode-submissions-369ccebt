class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        # island require a connected graph but not diagonally
        # undirected graph
        # acyclic
        # non-weighted
        # https://www.w3schools.com/dsa/dsa_theory_graphs.php
        cnt = 0

        # start from 0, 0 and do DFS, increasing i, j
        # mark each element as visited as we move
        rows, cols = len(grid), len(grid[0])
        visited = set()
        cnt = 0

        def bfs(r: int, c: int):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))
            while q:
                row, col = q.popleft()
                # [right, left, up, down]
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    i, j = row + dr, col + dc
                    if (
                        i in range(rows)
                        and j in range(cols)
                        and grid[i][j] == "1"
                        and (i, j) not in visited
                    ):
                        q.append((i, j))
                        visited.add((i, j))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    cnt += 1

        return cnt
