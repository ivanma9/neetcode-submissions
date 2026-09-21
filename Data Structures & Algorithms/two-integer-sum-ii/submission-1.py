class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        all the smaller numbers are on the left
        all the bigger numbers on the right
        1 2 6 7 8
        
        9 < 13
        so needs to get bigger by moving l ->
        2+8 < 13
        6 +8 < 13
        too big so needs to be smaller go <-r
        6 + 7 == 13 
        MATCH -> return l, 

        13
        psuedo
        init pointers on ends
        while pointers do not cross or touch
            check if elements at pointers == target
                return pointer indices
            else
                if sum < target:
                    we need to increase sum by moving
                    left pointer inward
                if sum > target
                    we need to decrease sum by moving
                    right pointer inward

        '''

                
        # init pointers on ends
        l =0
        r= len(numbers) -1

        # while pointers do not cross or touch
        while (l< r):
            # check if elements at pointers == target
            total = numbers[l] + numbers[r]
            if total == target:
        #         return pointer indices
                return [l+1,r+1]
        #     else
            else:
                if total < target:
        #         if sum < target:
        #             we need to increase sum by moving
        #             left pointer inward
                    l+=1
                else:
                    r-=1
        #         if sum > target
        #             we need to decrease sum by moving
        #             right pointer inward

