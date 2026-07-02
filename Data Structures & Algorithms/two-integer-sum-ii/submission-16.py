class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            two_sum = numbers[l] + numbers[r]
            if two_sum == target and numbers[l] != numbers[r]:
                    return [l + 1, r + 1]
            if two_sum > target:
                r -= 1
                continue
            l += 1
        