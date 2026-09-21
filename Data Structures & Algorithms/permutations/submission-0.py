class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        backtracking because we need a lot of comibations
        of choosing and not choosing elems
        all permutations will have same size as n
        so we we choose
        element or another element
        cant choose once taken
        we will be taking each permutation of the subarray

        
        1,2,3
        1       2       3
    [2,3].   [1,3]      [1,3]
    2    3.   1.  3.  1.  2
    [3] [2] [3].  [1] [2]. [1]
3.      2.    3.  1.  2.   1
    base case = []
    return []


    choose elem an element from nums.
    for elements in nums:
        take
        res.append(cur + elem + permute(backtrack[i:]))
        remove
'''
        res = []
        def backtrack(cur, leftovers):
            if leftovers == []:
                res.append(cur.copy())
                return
            for i,elem in enumerate(leftovers):
                #take elem
                cur.append(elem)
                backtrack(cur, leftovers[:i] + leftovers[i+1:])
                # remove so it can try with the next elem
                cur.pop() 

            
        backtrack([],nums)
        return res






