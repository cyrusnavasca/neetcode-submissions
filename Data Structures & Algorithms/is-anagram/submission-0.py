class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Analyzing string s
        seen1 = {}
        for i in range(len(s)):
            if s[i] in seen1:
                seen1[s[i]] += 1
            else:
                seen1[s[i]] = 1

        # Analyzing string t
        seen2 = {}
        for j in range(len(t)):
            if t[j] in seen2:
                seen2[t[j]] += 1
            else:
                seen2[t[j]] = 1

        return seen1 == seen2
 