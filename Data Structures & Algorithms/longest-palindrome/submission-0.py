class Solution:
    def longestPalindrome(self, s: str) -> int:
        # aba is a palindrome
        # For odd length strings: The outer characters must match
        # A pointer can be shifted inward to check them until a central

        # store character as key and count as value
        # if the all counts are even: palindrome
        # the same can be done if one of the counts is odd and the other two are even
        # but if there are two odd numbers, we need to choose one

        # Space: O(52) (26 + 26)
        # Time: O(n)

        max_len = 0
        # when a character is seen more than once, update max_len
        count = defaultdict(int)

        for c in s:
            count[c] += 1
            # if it's even, we update
            if count[c] % 2 == 0:
                max_len += 2
        
        print(count)

        for cnt in count.values():
            if cnt % 2:
                max_len += 1
                break

        return max_len