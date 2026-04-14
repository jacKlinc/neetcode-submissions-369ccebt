class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # return the list items that sum to zero
        # but indices i, j, k must be unique
        res = []  # key is sum of valuues of window start
        #l = 0
        # Helps eliminate duplicates: O(n.logn)
        nums.sort()
        # Now we can just do TwoSum
        for i, n in enumerate(nums):
            # Avoid using same value
            if i > 0 and n == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                three_sum = n + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                
        return res
        

