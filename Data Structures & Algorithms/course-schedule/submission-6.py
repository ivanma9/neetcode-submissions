class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        visited = set()
        def dfs(cur, path):
        # consider each courses children:

            path.add(cur)

            for c in adj_list[cur]:
                # cycle found
                if c in path:
                    return False
                if c in visited: # seen where c goes already
                    continue
                if not dfs(c, path):
                    return False
            
            path.remove(cur)
            # finished with no cycle at cur
            visited.add(cur)

            return True
        


        # determine if there is a cycle
        adj_list = defaultdict(list)
        # adj list
        for a,b in prerequisites:
            adj_list[b].append(a)

        # start from every course in numCourses
        for start in range(numCourses):
            # dfs 
            if not dfs(start, set()):
                return False

        return True
    