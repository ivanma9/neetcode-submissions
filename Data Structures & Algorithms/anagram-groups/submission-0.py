class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) 
        # hmap tuple of 26 char alphabet: [group of anagrams]
        
        for s in strs:
            count =[0] * 26
            for c in s:
                count[ord(c) - ord("a")] +=1
            res[tuple(count)].append(s)
        return res.values()