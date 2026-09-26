# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        k_indices = {e: i for i, e in enumerate(inorder)}
        self.pre_idx = 0

        def createTree(l, r):
            if l > r:
                return None

            root = preorder[self.pre_idx]
            self.pre_idx += 1
            # find k 
            k = k_indices[root]                
            node = TreeNode(root)
            node.left = createTree(l,k-1)
            node.right = createTree(k+1, r)
            return node
        return createTree(0,len(preorder)-1)
