# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        # bfs
        if not root: return []
        queue = deque([root])
        while(queue):
            layer = []
            n=len(queue)
            for _ in range(n):
                node = queue.popleft()
                # if node is None:
                #     continue
                layer.append(node.val)
                # add children
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(layer)
        return res
                


