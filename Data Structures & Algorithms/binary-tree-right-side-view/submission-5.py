# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # bfs because we just want one node each level
        # add the last item in queue to the output
        # do by level
        # while adding each child to queue
        if not root:
            return []
        res =[]
        queue = deque([root])
        while(queue):
            n = len(queue)
            for i in range(n):
                cur = queue.popleft()
                if i == n -1:
                    #last 
                    res.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            
        return res
