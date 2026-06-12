class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = int(0)
        p2 = len(numbers)-1
        while p1<p2 and numbers[p1]+numbers[p2]!=target:
            if numbers[p1]+numbers[p2]>target:
                p2-=1
                continue
            elif numbers[p1]+numbers[p2]<target:
                p1+=1
                continue
        return [p1+1,p2+1]