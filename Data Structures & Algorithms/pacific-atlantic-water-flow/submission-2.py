class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # strat is to go from each ocean inwards
        # run DFS on each value with the constraint that each sucessive value decreases
        # check each value is not in the visited sets
        res = []
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r: int, c: int, visited: Set, prev: int):
            """Marks all nodes that can reach an ocean"""
            if (
                (r, c) in visited
                or r not in range(rows)
                or c not in range(cols)
                or heights[r][c] < prev  # prev height needs to be bigger
            ):
                return

            visited.add((r, c))
            # run DFS on all four neighbours
            for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                dfs(r + dr, c + dc, visited, heights[r][c])

        # check top and bottom rows
        for c in range(cols):
            # need to pass in the previous height so that it has something to compare to
            dfs(0, c, pac, heights[0][c])  # first row
            dfs(rows - 1, c, atl, heights[rows - 1][c])  # last row

        # check left and right columns
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])

        # fill result
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res
