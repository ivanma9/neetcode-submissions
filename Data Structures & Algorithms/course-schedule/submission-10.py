class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for c,p in prerequisites:
            adj_list[p].append(c)

        visited = set()
        visiting = set()
        def dfs(c):
            if c in visited:
                return True
            if c in visiting:
                return False
            visiting.add(c)
            for nei in adj_list[c]:
                if not dfs(nei):
                    return False
            visiting.remove(c)
            visited.add(c)
            return True


        for i in range(numCourses):
            if not dfs(i):
                return False

        return True