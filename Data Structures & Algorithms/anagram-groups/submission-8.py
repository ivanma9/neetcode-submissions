class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key is tuple of letters in 26 char key
        hm = defaultdict(list)
        for word in strs:
            key = [0] * 26
            for l in word:
                key[ord(l) - ord('a')] +=1
            hm[tuple(key)].append(word)

        return [words for words in hm.values()]
