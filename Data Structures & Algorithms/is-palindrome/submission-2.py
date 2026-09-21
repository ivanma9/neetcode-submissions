class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l, r = 0, len(s) -1
        def isNotAlpha(c):
            return not c.isalnum()
        while (l<r):
            # if not alfanumeric skip
            while(l < r and isNotAlpha(s[l])):
                l +=1
            while(l < r and isNotAlpha(s[r])):
                r-=1
            print(s[l], s[r])
            if s[l] != s[r]:
                return False
            l,r = l+1, r-1

        return True