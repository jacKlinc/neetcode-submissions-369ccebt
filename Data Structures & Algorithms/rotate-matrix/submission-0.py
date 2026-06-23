class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # O(n²) time and O(1) memory 
        # i is the row index
        # j is the col index

        # The number of shifts in the outer layer will always be n - 1
        # Going into the inner matrix, the pointers can be shifted by 1
        # Replacing the values requires temp variables but there is a better way

        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r
                # save top left val in temp var
                top_left = matrix[top][l + i]

                # move bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # move bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # move top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                # move top left into top right
                matrix[top + i][r] = top_left
            r -= 1
            l += 1
                
        return 