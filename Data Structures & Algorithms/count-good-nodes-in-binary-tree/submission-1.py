# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # 
        # dfs
        def dfs(max_val, cur):
            if not cur:
                return 0
            ans = 1 if cur.val >= max_val else 0

            return ans + dfs(max(max_val, cur.val), cur.left) + dfs(max(max_val, cur.val), cur.right)

        return dfs(root.val,root)