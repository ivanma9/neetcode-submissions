class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        obs

                [1,2,0,1,0]
                 s n   n n true

                [1,2,1,0,1]
                 s n norn  false
                 paths 1 2 1 0
                 paths 1 2 0

                 brute force test out all paths from 0 to n
                 branching would O(n^n) worse case
                 O(5)(5)(5)(5)(5) n =1000
                 [4,3,3,1,0,1]
                  43210
                  4 210
                  4  10
                  4   0
                  43 10
                  43  0

                  backwards
                  1,0 nowhere
                  furthest index
                  [4 4 4 4 4 5]
                  max(nums[i] + jump[nums[i]])
                  max of the subarray
                  [4 4 5 4 4 5]

        '''

        n = len(nums)
        if n==1:
            return True
        jump = [0] * n
        jump[n-1] = n-1
        for i in range(n-2, -1,-1):
            
            jump[i] = max(jump[j] for j in range(i,min(i+nums[i]+1, n)))
    
        if jump[0] == n-1:
            return True
        return False
            
        
        
