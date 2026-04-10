class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        s_unique = set(s)
        t_unique = set(t)
        if s_unique != t_unique:
            return False
        for _s, _t in zip(s, t):
            if s.count(_s) != t.count(_s):
                return False
        return True
        #s_count = [s.count(_s) for _s in s]
        #t_count = [t.count(_t) for _t in t]
        #return s_count == t_count