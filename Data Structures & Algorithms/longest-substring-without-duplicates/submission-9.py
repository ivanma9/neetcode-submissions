class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # save a set of unique chars for the window

        res = 0
        l = 0

        bank = set()
        for r in range(len(s)):
            # eviction loop keep moving l until r is not in bank
            while(l <= r and s[r] in bank):
                
                bank.remove(s[l])
                l+=1
            # add r into bank
            bank.add(s[r])
            res = max(r - l + 1, res)

        return res
