class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res=-1
        for l in range(len(num)-2):
            if num[l] == num[l + 1] == num[l + 2]:
                res = max(res, int(num[l]))

        return str(res)*3 if res != -1 else ""
