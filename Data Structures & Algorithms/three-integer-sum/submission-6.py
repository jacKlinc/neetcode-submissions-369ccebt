class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, num in enumerate(nums):
            # check not the first value and not the same as previous element
            if i > 0 and num == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = num + nums[l] + nums[r]
                if three_sum == 0:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    # check the left num is not the same as the previous
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

                elif three_sum < 0:
                    l += 1
                else:
                    r -= 1

        return res