class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        substr = set()
        while r < len(s)-1:
            substr.add(s[l])
            if s[r+1] in substr: # if duplicate, slide
                l, r = l+1, r+1
            else: # if not duplicate, expand
                r += 1
                substr.add(s[r])

        print(substr)
        return len(substr)



        