class Solution:
    def characterReplacement(self, s: str, k: int) -> int:


        longest = 1
        highestFreq = 0


        freq = {}
        l = 0

        for r in range(len(s)):
            c = s[r]
            freq[c] = freq.get(c,0) + 1
            highestFreq = max(freq[c], highestFreq)

            

        
        
            while (r-l+1) - highestFreq > k:
                # remove until matches next char cuz we cant proceed with current hgihest freq s[r]
                highest = s[l]
                freq[highest] -=1
                l+=1
                # update longest
            longest = max(longest, r-l+1)
            


        return longest



        # lets track with a sliding window 
        # freq table of sliding table
        # letter with most will be priority for "streak"
        # look at first letter to see if its worth it to emit if not part of "streak" 
        



