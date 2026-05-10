class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Starting in the middle means comparison is possible from either side rather than just at the end
        # This reduces the time comlexity from O(n3) to O(n2)

        res = ""
        max_len = 0
        def find_palindrome(l: int, r: int, max_len: int, res: str):
            # l >= 0 and r < len(s): ensure its within bounds
            # s[l] == s[r]: is palindrome
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # (r - l + 1): length of the current substring is bigger than 
                if (r - l + 1) > max_len:
                    # update vars
                    res = s[l:r + 1]
                    max_len = r - l + 1
                # Move pointer away from centre
                l -= 1
                r += 1
            return max_len, res
        
        for i in range(len(s)):
            # Check odd length palindromes
            max_len, res = find_palindrome(i, i, max_len, res)
            # Check even length palindromes
            max_len, res = find_palindrome(i, i + 1, max_len, res)

        return res