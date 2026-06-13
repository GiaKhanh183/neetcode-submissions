class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best = int(0)
        i = int(0)
        j = len(heights)-1
        while i<j:
            area = min(heights[i],heights[j])*(j-i)
            if area>best:
                best = area
            if heights[i]>heights[j]:
                j-=1
            else:
                i+=1
        return best