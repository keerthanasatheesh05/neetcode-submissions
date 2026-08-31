class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        left = 0
        right = len(matrix) -1

        for i in range (len(matrix)):
            for j in range (len(matrix[i])):
                if target == matrix[i][j]:
                    return True
                
                elif target < matrix[i][j]:
                    left +=1

                else:
                    right -=1

        return False


