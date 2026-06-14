class Solution:
    def trap(self, height: List[int]) -> int:
        maxprefix = []
        maxsuffix = []
        maxheight = int(0)
        for i in range(len(height)):
            if height[i]>maxheight:
                maxheight = height[i]
                maxprefix.append(0)
            else:
                maxprefix.append(maxheight-height[i])
        maxheight=0
        maxsuffix = [0]*len(height)
        for j in range(len(height)-1,-1,-1):
            if height[j]>maxheight:
                maxheight = height[j]
                maxsuffix[j] = 0
            else:
                maxsuffix[j] = maxheight-height[j]
        totalarea= int(0)
        for k in range(len(height)):
            area = min(maxsuffix[k],maxprefix[k])
            totalarea+=area
        return totalarea

        