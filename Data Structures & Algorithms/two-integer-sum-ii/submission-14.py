class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while r < len(numbers):
            if numbers[l] + numbers[r] == target:
                if numbers[l] != numbers[r]:
                    return [l + 1, r + 1]
            if numbers[l] + numbers[r] > target:
                r -= 1
                continue
            l += 1
        