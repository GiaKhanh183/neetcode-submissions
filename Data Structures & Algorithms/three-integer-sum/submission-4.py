class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for k in range (1,len(nums)-1):
            i = k-1
            j = k+1
            while i>=0 and j<=len(nums)-1:
                if nums[i] + nums[k] + nums[j] < 0:
                    j+=1
                    continue
                elif nums[i] + nums[k] + nums[j] > 0:
                    i-=1
                    continue
                if nums[i] + nums[k] + nums[j] == 0:
                    if [nums[i],nums[k],nums[j]] in res:
                        i-=1
                        j+=1
                        continue
                    res.append([nums[i],nums[k],nums[j]])
                    i-=1
                    j+=1
                    continue
        return res
                