class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range (len(matrix)-1,-1,-1):
            if matrix[i][0]>target:
                continue
            for j in range (len(matrix[i])):
                if matrix[i][j] < target:
                    continue
                elif matrix[i][j] == target:
                    return True
        return False