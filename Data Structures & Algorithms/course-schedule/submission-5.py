class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # initialize prereqs dict
        prereqs = {}
        for i in range(numCourses):
            prereqs[i] = []

        # fill prereqs
        for post, pre in prerequisites:
            prereqs[post].append(pre)

        # check for cycle
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if prereqs[course] == []:
                return True
            visited.add(course)
            for pre in prereqs[course]:
                if dfs(pre) == False:
                    return False
            visited.remove(course)
            prereqs[course] = []
            return True

        
        for i in range(numCourses):
            if dfs(i) == False:
                return False
        
        return True

        