class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        longest = int(0)
        count = int(0)
        if len(nums)>0:
            count=1
            longest=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                count = count + 1
                if count > longest:
                    longest = count
            elif nums[i]>nums[i-1]+1:
                count = 1
        return longest



