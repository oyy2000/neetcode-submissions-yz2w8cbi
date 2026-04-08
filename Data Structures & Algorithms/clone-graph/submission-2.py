"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldNew = {}
        if not node:
            return None
        oldNew[node] = Node(node.val)
        q = deque([node])
        # q.append(node)
        while q:
            n = q.popleft()
            for nei in n.neighbors:
                if nei not in oldNew:
                    q.append(nei)
                    oldNew[nei] = Node(nei.val)
                oldNew[n].neighbors.append(oldNew[nei])

        return oldNew[node]
        
        