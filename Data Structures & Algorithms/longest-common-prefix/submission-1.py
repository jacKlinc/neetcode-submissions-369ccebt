class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_pre = ""

        # Iterate over first string
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return common_pre
            common_pre += strs[0][i]

        return common_pre