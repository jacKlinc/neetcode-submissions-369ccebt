class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Solution Notes:
        # Limited to uppercase: 26
        # We don't have to replace the string, rather return the count

        # We need to check if the sliding window is valid (number of repalcements <= k)
        res = 0 # longest window not necessarily length of input string
        char_freq = {}

        l = 0
        max_f = 0 # of the window
        for r in range(len(s)):
            # Increments character frequency
            char_freq[s[r]] = 1 + char_freq.get(s[r], 0)
            # find max frequency for window
            max_f = max(max_f, char_freq[s[r]])
            while (r - l + 1) - max_f > k:
                # decrement the char's frequency map for the window 
                char_freq[s[l]] -= 1
                # move the window
                l += 1
            # Store the result
            res = max(res, r - l + 1)
        return res    
        