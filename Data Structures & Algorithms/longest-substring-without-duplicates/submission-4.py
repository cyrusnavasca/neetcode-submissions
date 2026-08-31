class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        current = set()
        longest = 0

        while r < len(s):
            if s[r] not in current:
                current.add(s[r])
            else:
                while s[r] in current:
                    if s[l] in current:
                        current.remove(s[l])
                    l += 1
                current.add(s[r])
            r += 1

            longest = max(longest, len(current))
        
        return longest

        