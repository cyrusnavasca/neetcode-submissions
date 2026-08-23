class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        substr = set()
        longest = 0
        while r < len(s):
            if s[r] in substr:
                while s[r] in substr:
                    substr.remove(s[l])
                    l += 1
                substr.add(s[l])
            else:
                substr.add(s[r])
            r += 1

            if len(substr) > longest:
                longest = len(substr)

        return longest
