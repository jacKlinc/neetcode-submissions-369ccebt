class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Start right pointer at end of array to maximise area
        l, r = 0, len(heights) - 1
        product = 0
        # Volume = h*w. h = min(max(heights), next_biggest). w = indexof(max(heights)), indexof(next_biggest)
        # The product should be stored and updated

        # The left pointer cannot cross the right
        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            product = max(product, area)

            if heights[l] < heights[r]:
                l += 1            
            else:
                r -= 1
        return product
