class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0]
        res = [0]*len(temperatures)
        for i in range(1,len(temperatures)):
            if temperatures[i] <= temperatures[i-1]:
                stack.append(i)
            else:
                while stack and temperatures[stack[-1]] < temperatures[i]:
                    cursor = stack.pop()
                    res[cursor] = i-cursor
                stack.append(i)
        return res   