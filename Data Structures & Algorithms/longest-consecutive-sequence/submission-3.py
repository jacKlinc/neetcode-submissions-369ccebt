class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """if len(nums) == 1:
            return 1
        # Sorting: O(nlogn)
        nums.sort()
        sub_set = set()
        for i in range(1, len(nums)):
            current = nums[i]
            previous = nums[i - 1]
            if current == previous:
                sub_set.add(current)
            if current - 1 == previous:
                if current in sub_set:
                    continue
                sub_set.add(current)
                if previous in sub_set:
                    continue
                sub_set.add(previous)
        return len(sub_set)
        """
        # O(n) solution
        # Each sequence has no left neighbour
        nums_set = set(nums)
        max_len = 0
        for n in nums:
            # check for start of sequence
            if (n - 1) not in nums_set:
                length = 0
                while (n + length) in nums_set:
                    length += 1
                max_len = max(max_len, length)
        return max_len
