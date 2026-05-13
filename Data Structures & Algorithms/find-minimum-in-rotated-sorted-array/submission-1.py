class Solution:
    def findMin(self, nums: List[int]) -> int:
        # looks like a binary search
        # return min(nums) # O(n)
        res = nums[0]
        for n in nums:
            if n < res:
                res = n
        return res