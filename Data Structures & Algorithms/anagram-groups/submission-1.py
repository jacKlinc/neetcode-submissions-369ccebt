class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) < 2:
            return [strs]

        # store anagram in hash key to enforce uniqueness
        # store strings as values
        res = {}

        for s in strs:
            sorted_s = "".join(sorted(s))
            if not res or sorted_s not in res:
                res[sorted_s] = [s]
                continue
            res[sorted_s].append(s)

        return list(res.values())
