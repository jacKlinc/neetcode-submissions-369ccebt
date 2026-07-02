class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while r < len(numbers):
            #print(numbers[l], numbers[r])
            if numbers[l] + numbers[r] == target:
                if numbers[l] != numbers[r]:
                    return [l + 1, r + 1]
            print(l, r)
            if numbers[l] + numbers[r] > target:
                r -= 1
                #continue
            else:
                l += 1
        print(l, r)
        