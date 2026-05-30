class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        total = 0
        while i < len(heights) :
            j = len(heights)-1
            while j > i:
                water = (j-i) * min(heights[i],heights[j])
                if water > total:
                    total = water
                j = j-1
            i = i+1
        return total

        