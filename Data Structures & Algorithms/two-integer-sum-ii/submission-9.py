class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # when looping, we know the array is sorted
        # so when we reach an element that exceeds the target sum, we can exit loop

        # use two-pointer pattern
        l, r = 0, len(numbers) - 1
        while l < r:
            sum_vals = sum([numbers[l], numbers[r]])
            if sum_vals == target:
                return [l + 1, r + 1]
            # too big
            if sum_vals > target:
                r -= 1
                continue
            l += 1
        return
