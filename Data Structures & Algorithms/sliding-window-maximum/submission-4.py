class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        l = 0
        maxarray = []
        for r in range(len(nums)):
            heapq.heappush(heap, -nums[r])
            
            if r - l + 1 == k:
                heapq.heapify(heap)
                maxarray.append(-heap[0])
                heap.remove(-nums[l])
                l+=1

        return maxarray