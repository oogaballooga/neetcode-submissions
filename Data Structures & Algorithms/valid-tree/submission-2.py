class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        edgeDict = {i: set() for i in range(n)}
        for a, b in edges:
            edgeDict[a].add(b)
            edgeDict[b].add(a)
        
        visited = set()

        def dfs(num):
            if num in visited:
                return False
            visited.add(num)
            for neighbor in edgeDict[num]:
                edgeDict[neighbor].remove(num)
                if dfs(neighbor) == False:
                    return False

        if dfs(0) == False:
            return False

        return len(visited) == n