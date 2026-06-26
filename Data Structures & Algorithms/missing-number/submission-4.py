class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        max_num = max(nums)
        for i in range(max_num):
            if i != nums[i]:
                return i
        return max_num + 1