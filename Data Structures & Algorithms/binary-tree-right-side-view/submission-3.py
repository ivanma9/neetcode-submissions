# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''#bfs
        edge cases
        if no nodes -> print []
        if root only -> print []

        bfs need add by layer from right to left
        [3,2]
        need to process queue and getchildren of all the nodes in the queue
        only take top as result
        '''
        if not root:
            return []
        res = []
        queue = []
        queue.append(root)
        while(queue):
            n = len(queue)
            first_val = queue[0].val
            res.append(first_val)

            for _ in range(n):
                parent = queue.pop(0)

                if parent.right:
                    queue.append(parent.right)
                if parent.left:
                    queue.append(parent.left)
        return res


