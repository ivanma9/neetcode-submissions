# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        def check(root, low, high):
            if root is None:
                return True

            if root.left:
                if not (low < root.left.val and root.left.val < root.val):
                    return False
            if root.right:
                if not (root.val < root.right.val and root.right.val < high):
                    return False
            return check(root.left, low, root.val) and check(root.right, root.val, high)

        return check(root, float('-inf'), float('inf'))