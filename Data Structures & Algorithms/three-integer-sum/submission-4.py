class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # target here is 0
        # i, j, k must be distinct
        # O(n2) by looping over the lot


        res = []
        nums.sort()

        for i, n in enumerate(nums):
            # we don't same the same first value twice
            if i > 0 and n == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = n + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                    continue
                if three_sum == 0:
                    res.append([n, nums[l], nums[r]])
                l += 1
                # use loop to avoid having duplicate sums
                while nums[l - 1] == nums[l] and l < r:
                    l += 1
        return res