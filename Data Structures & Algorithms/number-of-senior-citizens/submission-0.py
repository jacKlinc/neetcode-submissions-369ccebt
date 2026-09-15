class Solution:
    def countSeniors(self, details: List[str]) -> int:
        cnt = 0
        for d in details:
            if int(d[11:13]) > 60:
                cnt += 1

        return cnt
