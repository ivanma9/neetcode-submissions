# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # all the nodes on the left of root inorder
        #
        # order of roots are in preorder

        # lets do a quick way to save root location
        root_indices = defaultdict(int)
        for i in range(len(inorder)):
            root_indices[inorder[i]] = i
        
        def dfs(pre, l, r):
            if len(pre) == 0:
                return None
            if l > r:
                return None
            root = pre.pop()
            r_index = root_indices[root]
            left = dfs(pre, l, r_index-1) 
            right = dfs(pre, r_index +1, r)
            t = TreeNode(root,left,right)

            return t

        
        
        return dfs(preorder[::-1], 0, len(inorder) - 1)
