class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hash map stores the unique chars and values are appended
        res={}
        for s in strs:
            key = "".join(sorted(s))
            if key in res:
                res[key].append(s)
                continue
            res[key] = [s]

        return list(res.values())