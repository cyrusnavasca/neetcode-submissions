class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        chars = {}
        for i in range(len(s)):
            if s[i] not in chars:
                 chars[s[i]] = 1
            else:
                chars[s[i]] += 1
        
        for j in range(len(t)):
            if t[j] not in chars:
                return False
            elif chars[t[j]] == 1:
                chars.pop(t[j])
            else:
                chars[t[j]] -= 1
        
        if len(chars) == 0:
            return True
        else:
            return False


