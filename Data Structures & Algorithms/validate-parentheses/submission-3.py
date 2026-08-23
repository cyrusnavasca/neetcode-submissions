class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        closed_map = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        open_set = set(["(", "[", "{"])

        for i, char in enumerate(s):
            if char in open_set:
                stk.append(char)
            else:
                if not stk:
                    return False
                elif closed_map[char] == stk[-1]:
                    stk.pop()
                else:
                    return False
        # unclosed bracket
        if stk:
            return False
            
        return True



        