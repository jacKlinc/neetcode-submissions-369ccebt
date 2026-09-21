class Solution:
    def minOperations(self, s: str) -> int:
        # the definition of alternating seems to be the flip flop between 0 and 1
        # could count when the current value does not equal the next
        cnt = 0
        for i in range(len(s)):
            if i % 2 == 0:
                cnt += 1 if s[i] == "0" else 0
            else:
                cnt += 1 if s[i] == "1" else 0

        return min(cnt, len(s) - cnt)
