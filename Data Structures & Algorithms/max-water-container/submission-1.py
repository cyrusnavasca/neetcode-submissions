class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest = 0
        # two-pointers approach
        l, r = 0, len(heights)-1
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            if area > largest:
                largest = area

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return largest