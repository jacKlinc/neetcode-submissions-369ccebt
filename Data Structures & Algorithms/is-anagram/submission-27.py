class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for c in set(s):
            if t.count(c) != s.count(c):
                return False

        return len(s) == len(t)
