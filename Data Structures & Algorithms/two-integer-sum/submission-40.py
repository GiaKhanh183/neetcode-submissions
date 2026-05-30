class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexed = []
        for i,j in enumerate(nums):
            indexed.append([j, i])
        
        i=0
        j=len(nums)-1
        indexed.sort()
        while i<j:
            currentsum = indexed[i][0] + indexed[j][0]
            if currentsum == target:
                break
            elif currentsum < target:
                i+=1
            elif currentsum > target:
                j-=1
        if indexed[i][1]<indexed[j][1]:
            return [indexed[i][1],indexed[j][1]]
        else:
            return [indexed[j][1],indexed[i][1]]