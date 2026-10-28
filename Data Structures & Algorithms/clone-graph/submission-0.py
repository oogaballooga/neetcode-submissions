"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        created = {}

        def search(oldNode):
            newNode = Node(oldNode.val, [])
            created[oldNode.val] = newNode
            for n in oldNode.neighbors:
                if n.val not in created:
                    search(n)
                newNode.neighbors.append(created[n.val])
            return newNode

        return search(node)