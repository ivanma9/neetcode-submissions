class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        # search for the row we should search in
        # based off first element

        row = -1
        #Olog(ROWS)
        l,r = 0,ROWS -1
        while(l<=r):
            mid = (l+r) //2
            midE = matrix[mid][0]
            nextE = matrix[mid+1][0] if mid != ROWS-1 else matrix[-1][-1] + 1 # last element + 1

        # if first element <= target and target < nextrow first element:
            if midE <= target and target < nextE:
                row = mid
                break
                # found
            elif midE > target:
                r = mid - 1
            else:
                l = mid + 1

        if row == -1:
            # outside max element
            return False
        
        # row is set; look thru cols binary O(logCOLS)
        l,r = 0,COLS -1
        while(l<=r):
            mid = (l+r) //2
            midE = matrix[row][mid]
            if midE == target:
                return True
            elif midE > target:
                r = mid -1
            else:
                l = mid+1
            
        return False
