class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            # A list of zeros for each char in alphabet
            count = [0]*26
            for c in s:
                # Increment the count for each character
                count[ord(c) - ord("a")] += 1
            # tuples are hashable if their elements are hashable
            # The tuple key is unique for each char combo
            res[tuple(count)].append(s)

        return list(res.values())
