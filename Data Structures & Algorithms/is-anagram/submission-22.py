class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_unique = set(s)
        for ss in s_unique:
            if t.count(ss) != s.count(ss):
                return False

        return len(s) == len(t)
