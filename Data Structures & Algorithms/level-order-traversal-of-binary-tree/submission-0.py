# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #bfs
        res = []
        queue = [root]
        while(queue):
            n = len(queue)
            level = []
            for _ in range(n):
                cur = queue.pop(0)
                if not cur:
                    continue
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                level.append(cur.val)
            if level:
                res.append(level)
        return res