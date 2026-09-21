# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #bfs
        # layer by layer new array 
        res = []
        if root is None:
            return []
        queue = [root]
        while queue:
            n = len(queue)
            layer = []
            for _ in range(n):
                cur = queue.pop(0)
                if cur is None:
                    print("N")
                    continue
                layer.append(cur.val)
                # add children to queue
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(layer)
        return res

