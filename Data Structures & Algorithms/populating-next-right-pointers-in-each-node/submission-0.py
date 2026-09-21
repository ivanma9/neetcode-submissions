"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # bfs
        queue = [root]
        while(queue):
            n = len(queue)
            prev = Node()
            layer = []

            for _ in range(n):
                #create Node
                node = queue.pop(0)
                if node is None:
                    continue
                print(node.val)

                prev.next = node
                print("prev",prev.val)
                prev = prev.next  
                print("prev after",prev.val)                             

                #add to q
                layer.append(node.left)
                layer.append(node.right)
            
            queue = layer
            # queue.extend(layer)

        return root