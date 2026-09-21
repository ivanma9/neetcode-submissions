class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        save a set of all the distinct chars
        can go left to right because contiguous
        move right pointer always
        move left pointer if left == right element
        track largest window: r - l +1
        and add to c to set
        '''
        l = 0 
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        distinct_set = set(s[0])
        maxL=1
        for r in range(1,len(s)):
            while s[r] in distinct_set:
                distinct_set.remove(s[l])
                l+=1
            maxL = max(maxL,r - l +1)
            distinct_set.add(s[r])
        return maxL
            