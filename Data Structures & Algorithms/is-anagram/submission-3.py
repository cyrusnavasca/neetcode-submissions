class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        l = 0
        checked1, checked2 = {}, {}
        while l < len(s):
            if s[l] in checked1:
                checked1[s[l]] += 1
            else:
                checked1[s[l]] = 1
            
            if t[l] in checked1:
                checked2[t[l]] += 1
            else:
                checked2[t[l]] = 1

            l += 1
        
        return checked1 == checked2



    