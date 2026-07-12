class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                ll = [num, nums[l], nums[r]]
                if sum(ll) == 0:
                    res.append(ll)
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                if sum(ll) < 0:
                    l += 1
                else:
                    r -= 1

        return res