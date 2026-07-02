class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()   # stores indexes
        result = []

        for r in range(len(nums)):
            # Remove smaller values from the back
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            # Add current index
            q.append(r)

            # Remove index if it is outside the window
            if q[0] <= r - k:
                q.popleft()

            # Start adding answers when first window is complete
            if r >= k - 1:
                result.append(nums[q[0]])

        return result