class Solution:
    def isPalindrome(self, s: str) -> bool:
        no_space_lower = s.replace(" ", "").lower()
        alpha_num = "".join(filter(str.isalnum, no_space_lower))
        return alpha_num[::-1] == alpha_num