class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # approach 1
        # get all the permutations of s1:
        # look for them in s2
        # O(m^2*n)

        # a2
        # create a letter freq
        # go thru s2, when i see a letter +=1 on s2freq
        # if len(s2freq) ==len(freq) true can use anew map
        # if we run into another char or passed freq(letter) is neg (too many ofthat letter) we slide the window until we see that character in left to balance
        # remove every char it sees on the way
        # O(m+ n)

        freq = Counter(s1)
        s2Freq = {k:0 for k in freq.keys()}
        print(s2Freq)
        
        l = 0
        for r in range(len(s2)):
            if s2[r] not in freq:
                s2Freq = {k:0 for k in freq.keys()}
                l=r+1
                continue
            else:
                s2Freq[s2[r]] += 1
                print(r, s2[r], s2Freq)
                if freq == s2Freq:
                    return True
                while l<=r and s2Freq[s2[r]] > freq[s2[r]]:
                    print(l, s2[l])
                    s2Freq[s2[l]] -= 1
                    l+=1

        return False




