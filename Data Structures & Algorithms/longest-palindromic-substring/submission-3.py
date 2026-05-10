class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Starting in the middle means comparison is possible from either side rather than just at the end
        # This reduces the time comlexity from O(n3) to O(n2)

        res = ""
        max_len = 0
        
        for i in range(len(s)):
            # Check odd length palindromes
            l, r = i, i
            def find_palindrome(l: int, r: int, max_len: int, res: str):
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    if (r - l + 1) > max_len:
                        res = s[l:r + 1]
                        max_len = r - l + 1
                    l -= 1
                    r += 1
                return max_len, res
            max_len, res = find_palindrome(l, r, max_len, res)
            # Check even length palindromes
            l, r = i, i + 1
            max_len, res = find_palindrome(l, r, max_len, res)

        return res