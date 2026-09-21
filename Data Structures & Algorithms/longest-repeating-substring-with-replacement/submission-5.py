class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #goal: return length of the longest substring  with only on char
        # K2
        # XYYX
        # window        evict len  maxletter
        # {X:1}.              1     X
        # {X:1, Y: 1}         2.    X
        # {X:1, Y:2}          3     Y
        # {X:2, Y:2}.         4.    Y

        # return 4

        # K1
        # AAABABB
        # window        evict len  maxletter
        # {A:1}.              1     A
        # {A:2}               2.    A
        # {A:3}                3     A
        # {A:3, B:1}.         4.    A
        # {A:4, B:1}          5       A
        # {A:1, B:2}.   AAA    3     B
        # {A:1, B:3 }        4      B
        # ret 5

        window = {}
        l =0

        res = 0
        maxCount = 0
        for r in range(len(s)):

            window[s[r]] = window.get(s[r], 0) + 1
            maxCount = max(maxCount, window[s[r]])


            #evict when 
            windowlen = r -l +1
            while l<r and windowlen - maxCount > k:
                window[s[l]] -=1
                l+=1
                windowlen = r -l +1

            res = max(res,windowlen)

        return res




