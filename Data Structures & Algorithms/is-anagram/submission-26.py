class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_unique = set(s)
        for c in s_unique:
            if t.count(c) != s.count(c):
                return False

        return len(s) == len(t)
