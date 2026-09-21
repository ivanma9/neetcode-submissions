class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            n = len(s)
            ans += str(n)
            ans += "#"
            ans += s
        return ans
        
    def decode(self, s: str) -> List[str]:
        print(s)
        ans = []
        i = 0
        while(i < len(s)):
            j= i
            # find out len of substr
            while (j < len(s) and s[j] != "#"):
                j+=1
            print("hi", i, j)
            print(s[i:j])
            length = int(s[i:j])
            ans.append(s[(j+1): (j + 1 + length)])
            i = j + 1 + length

        return ans
