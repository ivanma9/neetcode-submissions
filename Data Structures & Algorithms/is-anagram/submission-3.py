class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hashmap of each letter, see if each letter match
        # freq table
        # + for building, - for comparing
        if len(s) != len(t):
            return False

        hm = {}
        for l in s:
            if l not in hm:
                hm[l] = 0
            hm[l] += 1
        
        for l in t:
            if l not in hm:
                return False
            else:
                hm[l]-=1
                if hm[l] == 0:
                    del hm[l]
        return True