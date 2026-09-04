class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        count_map = {}
        longest = 0
        while r < len(s):
            # Increment current character in count map
            if s[r] in count_map:
                count_map[s[r]] += 1
            else:
                count_map[s[r]] = 1
            
            # Check if current window is valid
            highest_freq = max(count_map.values())
            total_length = r - l + 1
            if total_length - highest_freq > k:
            # If not valid, need to repeatedly increment left
                while total_length - highest_freq > k and l <= r:
                    count_map[s[l]] -= 1
                    l += 1
            
            # Keep track of longest satisfying substring
            longest = max(longest, r - l +1)
            
            r += 1
        
        return longest


            
