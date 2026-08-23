class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        letters = set()
        longest = 0
        while r < len(s):
            if s[r] in letters:
                while s[r] in letters and l <= r:
                    letters.remove(s[l])
                    l += 1

            letters.add(s[r])
            r += 1

            longest = max(longest, len(letters))
        return longest

        