class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dig_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",        
        }
        res = []
        if len(digits) < 1:
            return res
        
        def dfs(cur, i ):
            if i >= len(digits):
                res.append("".join(cur))
                return
            chars = dig_map[digits[i]]
            for c in chars:
                cur.append(c)
                i+=1
                dfs(cur, i)
                i-=1
                cur.pop()
        dfs([], 0)
        return res

        # grab each digit from digits
        # with each digit choose one char from dig_map[digit] of chars
        # track a current subarray
        # append character from mapping
        # move to the next index
        # until all indices have been reach -> add combination to res
        # remove character
