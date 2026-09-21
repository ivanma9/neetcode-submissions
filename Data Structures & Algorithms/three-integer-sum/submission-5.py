class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # brute force we go throught O(n^3)
        # can make a hashmap (sum of 2nums: [ele1, ele2])
            # this would be O(n^2)
            # search through nums (0(n)) for -n in hashmap 
            # total O(n^2)
        
        # sorting O(nlogn)
        nums.sort()
        n=len(nums)
        res = []
        for i in range(n):
            target = nums[i]
            if i != 0 and nums[i] == nums[i-1]:
                continue
            #search through right of that array
            l, r = i+1, n-1
            while(l<r):
                twosum = nums[l] + nums[r]
                if twosum + target == 0:
                    res.append([nums[l],nums[r], target])
                    r-=1
                    l+=1
                    while(l<r and nums[l] == nums[l-1]):
                        l+=1
                if twosum + target > 0:
                    r-=1
                if twosum + target < 0:
                    l+=1

        return res


