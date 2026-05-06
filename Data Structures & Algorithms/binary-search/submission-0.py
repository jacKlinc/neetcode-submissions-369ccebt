class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Must be sorted to use binary search
        # Find the middle and compare to target to choose traversal direction
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if target == nums[mid]:
                return mid

            # Ignore left
            if target > nums[mid]:
                low = mid + 1
                continue
                
            # Ignore right
            high = mid - 1
        return -1
            