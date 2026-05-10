class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Starting in the middle means comparison is possible from either side rather than just at the end
        # This reduces the time comlexity from O(n3) to O(n2)

        res = ""
        max_len = 0
        
        for i in range(len(s)):
            # Check odd length palindromes
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > max_len:
                    res = s[l:r + 1]
                    max_len = r - l + 1
                l -= 1
                r += 1
            # Check even length palindromes
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > max_len:
                    res = s[l:r + 1]
                    max_len = r - l + 1
                l -= 1
                r += 1

        return res