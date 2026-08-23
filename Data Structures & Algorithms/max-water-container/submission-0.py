class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest = 0
        # two-pointers approach
        l, r = 0, len(heights)-1
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            if area > largest:
                largest = area

            if heights[l+1] > heights[r-1]:
                l += 1
            else:
                r -= 1


        return largest