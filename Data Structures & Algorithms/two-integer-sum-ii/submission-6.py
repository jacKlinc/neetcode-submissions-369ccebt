class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 1-indexed means it starts at 1
        l = 0
        r = len(numbers) - 1
        while l < r:
            current_sum = numbers[l] + numbers[r] 
            if current_sum == target:
                return [l + 1, r + 1]
            
            # Move right pointer when sum more than target
            if current_sum > target:
                r -= 1
            elif current_sum < target:
                l += 1
        return