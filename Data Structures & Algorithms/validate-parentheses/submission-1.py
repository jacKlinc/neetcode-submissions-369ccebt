class Solution:
    def isValid(self, s: str) -> bool:
        if s[0] in ["]", "}", ")"]:
            return False
        # Could use the ordinal of each character
        # "[" is 91 and "]" is 93  
        # "{" is 123 and "}" is 125
        # but "(" is 40 and ")" is 41
        """parenthesis_map = {
            123: 125, # {}
            125: 123, # {}
            40: 41, # ()
            41: 40, # ()
            91: 93, # []
            93: 91 # []
        } 
        # could store the index of it, len - index could it's matching char
        for i, c in enumerate(s):
            closing = parenthesis_map[ord(c)]
            if chr(closing) not in s:
                return False

        return True"""

        # Removing each character after we've verified is best done with a Stack
        stack = []
        close_to_open = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for c in s:
            if c in close_to_open:
                # Check the last added item (-1) is the 
                if stack and stack[-1] == close_to_open[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
                     