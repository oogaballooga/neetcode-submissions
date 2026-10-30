class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #initialize and fill dict
        reqDict = {i: [] for i in range(numCourses)}
        for post, pre in prerequisites:
            reqDict[post].append(pre)

        #check for cycle
        visited = set()
        def dfs(course):
            if course in visited:
                return False

            if reqDict[course] == []:
                return True

            visited.add(course)

            for pre in reqDict[course]:
                if dfs(pre) == False:
                    return False
            visited.remove(course)

            reqDict[course] = []
            return True
            
        
        for course in range(numCourses):
            if dfs(course) == False:
                return False

        return True