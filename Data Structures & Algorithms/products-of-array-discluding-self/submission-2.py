class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n) solution 
        # Loop one direction and insert
        # Loop other direction and insert

        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            # Store initial multiplier here
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for  i in range(len(nums) - 1, -1, -1):
            # Multiply each element by what's already in the list
            res[i] *= postfix
            # shift postfix and mutiply
            postfix *= nums[i]

        return res