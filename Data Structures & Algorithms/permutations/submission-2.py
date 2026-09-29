class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(cur, i, cand_set):

            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            if i ==len(nums):
                return
            # consider all the candidates
            c= nums[i]

            if c not in cand_set:         
                cand_set.add(c)
                cur.append(c)
                backtrack(cur, 0, cand_set) # [1][2,3] start from beginning
                cur.pop()
                cand_set.remove(c)
            backtrack(cur,i+1, cand_set)
        
        backtrack([],0,set())
        return res
            

