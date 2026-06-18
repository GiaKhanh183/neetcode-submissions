class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = int(len(nums)/2)
        if target not in nums:
            return -1
        while nums[i] != target:
            if nums[i]<target:
                i+=1
            else:
                i-=1
        return i