class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        def dfs(u, par):
            visited.add(u)
            for v in adj[u]:
                if v == par:
                    continue

                if v in visited or not dfs(v, u):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n