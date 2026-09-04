class Solution:
    def isValid(self, s: str) -> bool:
        # {closed: open}
        bracket_map = {")": "(", "]": "[", "}": "{"}
        stk = []

        # iterating through characters
        for char in range(len(s)):
            # is character CLOSED?
            if char in bracket_map:
                # check if it matched current open bracket
                if stk[-1] != bracket_map[char] or not stk:
                    return False
                else:
                    stk.pop()

            # is character OPEN? -> append to stack
            else:
                stk.append(char)
            
        return True
        