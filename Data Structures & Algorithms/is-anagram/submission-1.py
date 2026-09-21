class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm = [0] * 26
        for ss in s:
            hm[ord(ss)-ord('a')] += 1
        for tt in t:
            hm[ord(tt)-ord('a')] -= 1

        for h in hm:
            if h != 0:
                return False
        return True