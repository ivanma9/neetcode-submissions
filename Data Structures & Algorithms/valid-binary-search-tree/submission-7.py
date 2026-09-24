# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # bounds are -inf,inf

        def valid(left_bound, right_bound, root):

            if root is None:
                return True
            if not (left_bound < root.val < right_bound):
                return False
            
            # if root.left and root.left.val >= root.val:
            #     return False 
            # if root.right and root.val >= root.right.val and root.val:
            #     return False
            return valid(left_bound,root.val,root.left) and valid(root.val, right_bound, root.right)
        return valid(float('-inf'),float('inf'), root)