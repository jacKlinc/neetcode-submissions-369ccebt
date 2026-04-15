class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        idx = range(len(nums))
        for i in idx:
            res = 1  # if n != 0 else 0
            for j in idx:
                if i != j:
                    res *= nums[j]
            output.append(res)
        return output