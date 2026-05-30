class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        settest = set(nums)
        if len(settest) == len(nums):
            return False
        else:
            return True