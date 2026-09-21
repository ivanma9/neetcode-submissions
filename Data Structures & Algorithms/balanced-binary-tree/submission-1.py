# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # need to know height
        # 
        # base case: leaf node -> return (True, 0)
        def dfs(node):
            if node is None:
                return (True,0)
                        # true and a height of 0

            if node.left is None and node.right is None:
                return (True,0)
            
        # left height (recurse) should be same thing to left +1
            left_h, right_h = 0,0
            left_balanced, right_balanced = True, True
            if node.left:
                left_balanced,left_height = dfs(node.left)
                left_h = 1 + left_height
                   # same for right
            if node.right:
                right_balanced,right_height = dfs(node.right)
                right_h = 1 + right_height
                right_h = 1 + dfs(node.right)[1]
        # subtract diff between left height and right height
            diff = abs(left_h - right_h)
            if diff > 1:
                return (False, max(left_h,right_h))
            return (left_balanced and right_balanced, max(left_h,right_h))

        # if diff is > 1 return false
        # else:
            # add 1 to child's height
        
        return dfs(root)[0]
