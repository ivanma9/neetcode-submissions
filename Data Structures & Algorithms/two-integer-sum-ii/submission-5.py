class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #sorted
        #return 1 index
        resl,resr = -1,-1

        l,r= 0, len(numbers) -1
        # no l =r because cant use same element twice
        while(l<r):
            twosum = numbers[l] + numbers[r]
            if twosum == target:
                return [l+1,r+1]

            # pinch left side if need to get bigger
            if twosum < target:
                l+=1

            # pinch right if need to get smaller
            if twosum > target:
                r-=1
        return [-1,-1]

        # [1,2,3,4] t 3

        # l 0, r 3
        # twosum = 1+4 = 5 > 3
        # l 0, r 2
        # twosum = 1+3 = 4 > 3
        # l 0, r 1
        # twosum = 1+2 = 3= 3 return 1,2


