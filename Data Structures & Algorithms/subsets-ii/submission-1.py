class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # no dupes
        res_set = set()
        nums.sort()
        def backtrack(cur, i):
            res_set.add(tuple(cur.copy()))


            for j in range(i,len(nums)):
                cur.append(nums[j])
                backtrack(cur, j+1)
                cur.pop()


        

        backtrack([], 0)

        return [list(e) for e in list(res_set)]
            # [1] [23]
            # [] [123]
            #     [1]
            #     [2]
            #     [3]