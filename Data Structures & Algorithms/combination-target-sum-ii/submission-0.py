class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []

        # if you do want dupe combinations from using the same element later (1,7) and (7,diff 1) 
        # then SORT elements and move pointer until not that ele.
        
        # take or not take
        # if sum is target add
        # above do not take
        candidates.sort()

        #take
        def dfs(i, cur, s):
            if (s == target):
                ans.append(cur.copy())
                return
            if (i == len(candidates) or s > target):
                return
            if (s < target):
                #take
                cur.append(candidates[i])
                dfs(i+1, cur,candidates[i] + s)
                cur.pop()
            
                # skip cand (dont take) i <= candidates - 1 -1
                while (i + 1 < len(candidates) and candidates[i] == candidates[i+1]):
                    i+=1
                dfs(i+1, cur, s)

        dfs(0,[],0)
        return ans