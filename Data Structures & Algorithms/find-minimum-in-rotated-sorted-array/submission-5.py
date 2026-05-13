class Solution:
    def findMin(self, nums: List[int]) -> int:
        # looks like a binary search
        # return min(nums) # O(n)
        
        # Could find the break where numbers stop ascending
        # This indicates end of sorted array
        
        # The question is if the middle pointer is in left or right sorted portion
        # Due to the nature of a rotated search, the largest value will be put at the start
        # Solution: if in left portion, look right

        # How do we know we're in the left?
        # If the middle value => left most value

        low, high = 0, len(nums) - 1
        res = nums[0]
        while low <= high:
            if nums[low] < nums[high]:
                res = min(res, nums[low])
                break
            
            mid = (high + low) // 2
            res = min(res, nums[mid])
            # Check in left portion
            if nums[mid] >= nums[low]:
                # Search right  
                low = mid + 1
                continue
            # Search left
            high = mid - 1
            
        return res