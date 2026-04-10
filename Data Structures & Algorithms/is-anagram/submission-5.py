class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_unique = set(s)
        t_unique = set(t)
        if s_unique != t_unique:
            return False
        # We already know that they have the same unique chars
        for u in s_unique:
            if s.count(u) != t.count(u):
                return False
        return True