# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxVal):
            if not node:
                return 0
            maxV = max(node.val, maxVal)
            res = 0
            if node.val >= maxVal:
                res +=1
            return res + dfs(node.left, maxV) + dfs(node.right, maxV)
        
        return dfs(root, root.val)
          
