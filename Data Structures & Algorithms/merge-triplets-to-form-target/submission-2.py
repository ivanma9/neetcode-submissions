class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        if len(triplets) == 1:
            aa,bb,cc = triplets[0]
            a, b, c = target
            return aa == a and bb == b and cc == c
        for i in range(1,len(triplets)):
            a1,b1,c1 = triplets[i-1]
            a2,b2,c2 = triplets[i]

            aa = max(a1,a2)
            bb = max(b1,b2)
            cc = max(c1,c2)
            a, b, c = target


            if aa == a and bb == b and cc == c:
                return True
            # lower and progressing let's still use this
            if aa <= a and bb <= b and cc <= c:
                triplets[i] = [aa,bb,cc]
            else:
                # do not use max and use smaller of the two
                if a1 <= a and b1 <= b and c1 <= c:
                    triplets[i] = [a1,b1,c1]
                # otherwise use a2,b2,c2 
        return False

