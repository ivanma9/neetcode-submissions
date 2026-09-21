class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # m max letters in str
        # n len(strs)
        # make a hm for all str (o(n*m))
        # hms key is the hm (NOT POSSIBLE)
        hms = {}
        for s in strs:
            hm = [0] * 26
            for l in s:
                hm[ord(l) - ord('a')] += 1
            hm_key = tuple(hm)
            if hm_key not in hms:
                hms[hm_key] = []
            hms[hm_key].append(s)


        return list(hms.values())
            
