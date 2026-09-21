# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #find p and find q. p!=q, always exist, 2 nodes        
        
        # if p or q is the node return node

        if root.val == p.val:
            return p
        if root.val == q.val:
            return q
        # if p and q are on opp sides of a node then return node
        if (p.val < root.val and root.val < q.val) or (q.val < root.val and root.val < p.val):
            return root
        
        # if p and q are on same side traverse that side
        # left
        res = root
        if p.val < root.val and q.val < root.val:
            res = self.lowestCommonAncestor(root.left, p, q)
        # right
        if p.val > root.val and q.val > root.val:
            res = self.lowestCommonAncestor(root.right, p, q)
        return res
        

