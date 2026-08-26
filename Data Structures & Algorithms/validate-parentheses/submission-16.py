class Solution:
    def isValid(self, s: str) -> bool:
        # if the length is odd it must be false
        if len(s) % 2 != 0:
            return False

        par_map = {"]": "[", ")": "(", "}": "{"}
        stack = []
        # Pop off the stack until empty
        for c in s:
            print(stack)
            # Closing bracket
            if c in par_map:
                # If not empty and top matches the opening bracket
                if stack and stack[-1] == par_map[c]:
                    stack.pop()  # pop and move on
                    continue
                return False
            # Push opening bracket onto stack
            stack.append(c)

        return not stack
