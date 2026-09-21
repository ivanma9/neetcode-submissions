class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # O(log(m*n))

        #search as if  big
            

                
        
        
        # do binary twice
        left = 0 
        right = len(matrix) - 1
        row_n = len(matrix[0]) - 1
        while (left <= right):
            mid_row = (right + left) // 2
            
            # if the row ele is > target
            if (matrix[mid_row][0] > target):
                #search less
                right = mid_row - 1
            else:
                # if greater and greater than last element in row
                if (matrix[mid_row][row_n] < target):
                    #search more
                    left = mid_row + 1
                else: 
                    break
                    # I am in the correct row
        l = 0
        r = row_n
        while (l <= r):
            mid = (l+r) // 2
            if (matrix[mid_row][mid] == target):
                #found
                return True
            if (matrix[mid_row][mid] > target):
                r = mid - 1
            else:
                l = mid + 1
        
        return False
