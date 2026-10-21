class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            k = [0]*26
            for l in s:
                k[ord(l) - ord('a')] +=1
            anagrams[tuple(k)].append(s)
        return list(anagrams.values())
                