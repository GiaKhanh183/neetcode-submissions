class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        time = []
        fleet = int(1)
        for i in range(len(position)):
            stack.append([position[i],speed[i]])
        stack.sort()
        for i in range(len(position)):
            time.append((target-stack[i][0])/stack[i][1])
        for i in range(len(position)-1,-1,-1):
            if time[i]<time[i-1]:
                fleet += 1
            else:
                time[i-1] = time[i]
            
        return fleet