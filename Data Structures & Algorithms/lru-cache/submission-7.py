class Node:
    def __init__(self, key=0, val=0, nextNode=None, prev=None):
        self.key = key
        self.val = val
        self.next = nextNode
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.dummyHead = Node()
        self.dummyTail = Node()
        self.dummyHead.next = self.dummyTail
        self.dummyTail.prev = self.dummyHead
        self.nodes = {} # (key : Node)
        self.capacity = capacity

    def addToTail(self, node: Node):
        # add to tail
        old_mru = self.dummyTail.prev
        self.dummyTail.prev = node
        node.next = self.dummyTail
        node.prev = old_mru
        old_mru.next = node
    
    def removeNode(self,node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        

    def get(self, key: int) -> int:
        if key in self.nodes:
            node = self.nodes[key]
            # remove node
            self.removeNode(node)


            self.addToTail(node)
            
            return node.val
        else:
            return -1

        

    def put(self, key: int, value: int) -> None:


        if key in self.nodes:
            # update
            oldNode = self.nodes[key]
            oldNode.val = value
            self.removeNode(oldNode)
            self.addToTail(oldNode)
        else:
            #add new
            newNode = Node(key, value)
            self.nodes[key] = newNode
            self.addToTail(newNode)

        if self.capacity < len(self.nodes):
            # evict lru
            lru = self.dummyHead.next
            self.removeNode(lru)
            del self.nodes[lru.key]
