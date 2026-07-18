class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        par_map = {"]": "[", "}": "{", ")": "("}
        stack = []
        
        for c in s:
            if c in par_map:
                if stack and stack[-1] == par_map[c]:
                    stack.pop()
                    continue
                return False
            stack.append(c)

        return not stack
