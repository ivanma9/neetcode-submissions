class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_parsed = s.upper()
        l,r = 0, len(s_parsed) - 1
        alphanum = set()
        for i in range(0,10):
            alphanum.add(str(i))
        for i in range(0,26):
            alphanum.add(chr(i+ 65))

        while(l<r):

            while l < r and s_parsed[l] not in alphanum:

                l+=1
            while l < r and s_parsed[r] not in alphanum:
                r-=1
            if s_parsed[l] == s_parsed[r]:
                l+=1
                r-=1
            else:
                return False
            


        return True