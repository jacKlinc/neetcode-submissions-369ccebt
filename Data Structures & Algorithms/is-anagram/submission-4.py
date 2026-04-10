class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        s_unique = set(s)
        t_unique = set(t)
        if s_unique != t_unique:
            return False
        for u in s_unique:
            if s.count(u) != t.count(u):
                return False
        return True