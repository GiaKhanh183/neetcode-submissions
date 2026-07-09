class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        test = set()
        for i in range(len(nums)):
            if nums[i] in test:
                return nums[i]
            test.add(nums[i])
        return -1