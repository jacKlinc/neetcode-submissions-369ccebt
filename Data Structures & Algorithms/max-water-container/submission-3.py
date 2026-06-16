class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # pointer problem
        l, r = 0, len(heights) - 1
        max_area = 0
        while l < r:
            print(l, r)
            # min of both heights to prevent water spilling
            area = min(heights[l], heights[r]) * (r - l)
            max_area = max(max_area, area)
            # how to increment?
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
            

        return max_area