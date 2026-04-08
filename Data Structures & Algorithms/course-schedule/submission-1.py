class Solution:

    valid = True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            edges[course].append(pre)
        visited = [0] * numCourses

        def dfs(u): 
            if visited[u] == 1:
                return False
            if visited[u] == 2:
                return True

            
            visited[u] = 1
            for v in edges.get(u):
                if not dfs(v):
                    return False
            visited[u] = 2
            return True
        

        for i in range(numCourses):
            if visited[i] == 0:
                if not dfs(i):
                    return False
        return True