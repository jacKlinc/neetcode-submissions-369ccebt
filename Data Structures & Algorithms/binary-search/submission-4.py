class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) 
        for i, num in enumerate(nums):
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                low = mid
                continue
            high = mid            

        return -1