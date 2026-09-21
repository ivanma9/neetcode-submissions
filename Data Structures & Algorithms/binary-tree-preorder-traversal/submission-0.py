# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #base
        res = []
        def dfs (root):
            if root is None:
                return

            # add to output
            res.append(root.val)
                        # go left
            dfs(root.left)
            # go right
            dfs(root.right)
        dfs(root)
        return res