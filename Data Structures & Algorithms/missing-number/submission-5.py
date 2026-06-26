class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """nums.sort() # O(n logn)
        max_num = max(nums) # O(n)
        for i in range(max_num): # O(n)
            if i != nums[i]:
                return i
        return max_num + 1"""
        res = len(nums)

        for i in range(len(nums)):
            res += (i - nums[i])
        
        return res