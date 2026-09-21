class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # make a dict of the characters of lowercase chars
        # if the dicts match than they are anagrams
        if len(s) != len(t):
            return False
        letters = [0] * 26
        for c in s:
            letters[ord(c) - ord('a')] += 1
        for c in t:
            if letters[ord(c) - ord('a')] <= 0:
                return False
            letters[ord(c) - ord('a')] -=1
        return True
            
        
