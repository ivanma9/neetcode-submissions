class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        # create a freq table s1
        s1_counts = Counter(s1)
        print(s1_counts)


        # init freqs2
        s2_counts = {}

        for i in range(len(s1)):
            letter = s2[i]
            s2_counts[letter] = s2_counts.get(letter,0) +1

        # go through s2 with windowsize of lens1
        for i in range(len(s1), len(s2)):
            print(s2_counts)
            # if window matches freq
            if s1_counts == s2_counts:
                return True

            # add next char
            s2_counts[s2[i]] = s2_counts.get(s2[i],0) +1
            #remove prev char
            s2_counts[s2[i-len(s1)]] -=1
            if s2_counts[s2[i-len(s1)]] == 0:
                del s2_counts[s2[i-len(s1)]]

        if s1_counts == s2_counts:
            return True

        return False

# s1="ab"
# s2="lecabee"

# s1 {a:1,b:1}
# s2 {l1,e1}
# i   chr    s2counts 
# 2.  c.    {e1,c1}
# 3.  a.    {c1,a1}
# 4.  b.    {a1,b1} return True
# 5.  e  





