class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Could sort each string and use it as a marker for an anagram
        # This would give a time complexity of O(m.n.log(n)) where n is the average str length and m the the number of strings

        # One of the constraints is that the str are a-z lowercase (26)
        # "cat" has 1 "c", 1 "a" and 1 "t". The same for "act"
        # The character count is the HashMap key and the value are the strings
        # Time complexity: O(m.n.26)

        d = defaultdict(list) # initialize with list as values
        for s in strs:
            count = [0] * 26  # a-z
            for c in s:
                # Increments count of that character
                count[ord(c) - ord('a')] += 1
            # A tuple needs to be used because a hash map key needs to be immutable
            d[tuple(count)].append(s)

        return list(d.values())