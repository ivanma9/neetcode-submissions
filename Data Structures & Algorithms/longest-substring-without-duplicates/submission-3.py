class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        l pointer - first char
        r pointer - newest char

        [l,r] there should be no dupes
        
        longest = 0
        '''

        longest = 0
        l = 0
        chars = set()
        for r in range(len(s)):
            while l < r and s[r] in chars:

                left_char = s[l]
                chars.remove(left_char)
                l+=1
            longest = max(r - l + 1, longest)
            chars.add(s[r])
        return longest
        # 0 []
        # 1 [x]

