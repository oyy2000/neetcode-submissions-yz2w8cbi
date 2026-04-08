class Solution:

    valid = True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            edges[course].append(pre)
        visited = [0 for _ in range(numCourses)]

        def dfs(u): 
            visited[u] = 1
            for v in edges.get(u):
                if (visited[v] == 0): 
                    dfs(v)
                elif visited[v] == 1:
                    self.valid = False;
            visited[u] = 2
        

        for i in range(numCourses):
            dfs(i)
        return self.valid