class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # save a set of unique chars for the window
        l = 0
        res = 1
        if s =="":
            return 0
        bank = set([s[0]])
        for r in range(1,len(s)):
            # eviction loop keep moving l until r is not in bank
            while(l <= r and s[r] in bank):
                
                bank.remove(s[l])
                l+=1
            # add r into bank
            bank.add(s[r])
            res = max(r - l + 1, res)

        return res
