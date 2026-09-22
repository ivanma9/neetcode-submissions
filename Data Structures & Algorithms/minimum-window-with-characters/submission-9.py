class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        res = ""
        # freq of t

        t_freq = Counter(t)

        windowLen = len(s) + 1 #minimize

        window = {} # only will have  chars in t
        need = len(t_freq)
        have = 0

        # expand window until we have a valid window
        l=0
        for r in range(len(s)):
            # is it in t?            
            if s[r] in t_freq:
                window[s[r]] = window.get(s[r],0) + 1
                if window[s[r]] == t_freq[s[r]]:
                    have +=1

                #evict to optimize

                while s[l] not in t_freq or window[s[l]] > t_freq[s[l]]: 
            # then optimize by evicting while valid until min
                    if s[l] in window:
                        window[s[l]]-=1
               
                    l+=1
            
                # calc with shortest Valid window
                            
                if have == need:
                    if r-l+1 < windowLen:
                        windowLen = r-l+1
                        res = s[l:r+1]

        if windowLen == len(s) + 1:
            return ""
        
        return res


        # t_freq {X:1, Y1, Z1}
        
        # UZODYXAZV
        # r  c  window   res. evict
        # 0     U         10. 
        # 1. Z  UZ
        # 2. O  UZO
        # 3  D  UZOD
        # 4. Y  UZODY
        # 5. X  ZODYX.    5. U
        # 6. A. ZODYXA    5  
        # 7. Z. YXAZ.     4   ZOD
        # 8. V  YXAZV     4
 
        # # evict when not in t OR
        # # evict when s[l] is > t_freq[s[l]]
        # if s[l] not in t_freq or window[s[l]] > t_freq[s[l]]:

