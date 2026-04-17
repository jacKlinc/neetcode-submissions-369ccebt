class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Start right pointer at end of array to maximise area
        l, r = 0, len(heights) - 1
        product = 0
        # Volume = h*w. h = min(max(heights), next_biggest). w = indexof(max(heights)), indexof(next_biggest)
        # The product should be stored and updated

        # The left pointer cannot cross the right
        while l < r:
            # w = difference in pointer position. h = smallest of the heights
            area = (r - l) * min(heights[l], heights[r])
            # Update product
            product = max(product, area)
            # Move the pointer left if smaller than right one
            if heights[l] < heights[r]:
                l += 1            
            # Keep the left pointer and move the right pointer
            else:
                r -= 1
        return product
