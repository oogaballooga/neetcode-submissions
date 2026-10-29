class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graphCount = 0
        visited = set()
        edgeDict = {i: set() for i in range(n)}
        for pre, post in edges:
            edgeDict[pre].add(post)
            edgeDict[post].add(pre)

        def dfs(num):
            if num in visited:
                return
            
            visited.add(num)
            for neighbor in edgeDict[num]:
                dfs(neighbor)
            

        for num in range(n):
            if num not in visited:
                graphCount += 1
                dfs(num)
        
        return graphCount