class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # {character: frequency in window}
        count_map = {}
        l, r = 0, 0
        longest = 0

        while r < len(s):
            # 1) increase count of s[r] in count map
            if s[r] in count_map:
                count_map[s[r]] += 1
            else:
                count_map[s[r]] = 1
            # 2) check if window is valid
            window_size = r - l + 1
            most_freq = max(count_map.values())
            if window_size - most_freq > k:
                # 3) increment when invalid
                count_map[s[l]] -= 1
                l += 1
                window_size -= 1

            r += 1

            longest = max(longest, window_size)
        return longest

        

                
        