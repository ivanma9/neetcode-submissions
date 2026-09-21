class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap (alphakey, list anagrams)
        anagrams = {}
        # turn every word into a hashable key of alhpabet tuple
        for word in strs:
            alpha = [0]*26
            for s in word:
                alpha[ord(s)-ord('a')] +=1
            
            alpha_key = tuple(alpha)
            if alpha_key not in anagrams:
                anagrams[alpha_key] = []
            anagrams[alpha_key].append(word)


            #constraints
        # can hv 1 word at least
        # string of words can be none (0,...0)


        # convert hashmap into a list of list
        res = [v for v in anagrams.values()]
        return res
