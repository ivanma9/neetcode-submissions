class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # len
        # order doesnt matter lets use set
        bank = set(nums)

        res = 0


        for x in nums:
        # if we find the number before its not the starting of LCS
        # if we find the number after it has more numbers to count     
            # looking for starting
            if x - 1 in bank:
                continue
            # found starting
            length = 1
            while((x + length) in bank):
                length +=1
            res = max(length,res)

        return res