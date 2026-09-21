# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # traverse at the same time
        # lets do dfs recursion
        # so we will check 
        # base case:
        # if p none and q none:
        if p is None and q is None:
            return True
        #     True
        # if only one none and other has node:
        if p is None or q is None:
            return False
        #     False
        # now both have node
        if p.val != q.val:
            return False
        # check if nodes have same value
        # only need one false
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)