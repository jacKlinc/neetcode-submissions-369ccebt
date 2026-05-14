class Solution:
    # How do we figure out which side of the sorting we're in?
    # The stuff at the front of the list will be the biggest
    # This means the mid index is not really the mid, 
    #   rather just halfway through the array, not halfway in the sort

    # mid = 3 (6)
    # [3,5,6,0,1,2]: the left most is the smallest of the larger portion (right)
    #   if the target is bigger than the leftmost, search the left portion
    #   if it smaller, search right

    # if in right side, the right most will element will be the biggest

    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (high + low) // 2

            if nums[mid] == target:
                return mid

            # Checks left
            if nums[mid] >= nums[low]:
                if target > nums[mid] or target < nums[low]:
                    # Search right
                    low = mid + 1
                    continue
                high = mid - 1
                continue
            if target < nums[mid] or target > nums[high]:
                high = mid - 1
                continue
            low = mid + 1

        return -1