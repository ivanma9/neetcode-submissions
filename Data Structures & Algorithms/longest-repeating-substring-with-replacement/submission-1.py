class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        alpha = defaultdict(int)
        ans = k
        l = 0
        for r in range(len(s)):
            alpha[s[r]] +=1
            max_c = max(alpha.values())
            length =r - l +1
            if max_c + k >= length:
                ans = max(max_c + k, ans)
            else:
                alpha[s[l]] -=1
                l+=1
        return min(len(s), ans)

