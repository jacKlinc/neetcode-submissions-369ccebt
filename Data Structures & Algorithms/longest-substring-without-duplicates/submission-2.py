class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_s = set()
        l = 0
        max_len = 0
        # check each character is in the unique list
        for r in range(len(s)):
            while s[r] in unique_s:
                # restart the list with the current element at the start
                unique_s.remove(s[l])
                l += 1
            # If it's unique, add it to the list
            unique_s.add(s[r])
            # Update the max length if it exceeds the current max
            max_len = max(r - l + 1, max_len)

        return max_len