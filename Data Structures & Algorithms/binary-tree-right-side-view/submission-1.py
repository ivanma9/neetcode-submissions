# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # traverse through every right node on every right subtree
        # track the level we have alread printed one
        #OHHH wait
        # we traverse level by level bfs
        # append value of last iterm to be added if we add l->r
        res = []
        # edge case:
        if root is None:
            return []
        # if root aloen return root

        queue = [root]
        while queue:
        #     for every element in the q:
            n = len(queue)
            for i in range(n):
                front = queue.pop(0)
        #         if last element in q:
                if i == n-1:
        #             add to res
                    res.append(front.val)
        #         add all left and right node only if they exist
                if front.left:
                    queue.append(front.left)
                if front.right:
                    queue.append(front.right)
        return res
