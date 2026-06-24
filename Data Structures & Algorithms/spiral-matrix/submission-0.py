class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # could iterate down until a number of cells goes to zero
        # It takes the permiter until it runs out and goes inward
        # 3x3 cell: 7 iterations before going inward (9 cells total): 9 - 7 = 2
        # 4x4 cell: 13 iterations before going inward (16 cells total): 16 - 13 = 3
        # could there be a pattern here?
        # 5x5 cell:  iterations before going inward (25 cells total)

        # O(n x m)
        # Arrays seem to use the l, r, top and bottom pointers to traverse
        l, r = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        res = []

        while l < r and top < bottom:
            for i in range(l, r):
                res.append(matrix[top][i])
            top += 1
            # get each i in the right column
            for i in range(top, bottom):
                res.append(matrix[i][r - 1])
            r -= 1

            if not (l < r and top < bottom):
                break

            # get each i in bottom row backwards
            for i in range(r - 1, l - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            # get each i in the left column
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][l])
            l += 1
        return res

