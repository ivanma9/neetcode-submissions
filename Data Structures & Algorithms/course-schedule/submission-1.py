class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


        #top sort
        adj_list = defaultdict(list)
        for a,b in prerequisites:
            adj_list[a].append(b)

        def dfs(i, visited):
            if i in visited:
                return False
            visited.add(i)
            for child in adj_list[i]:
                if not dfs(child, visited):
                    return False
            visited.remove(i)
            return True
        
        for i in range(numCourses):
            if not (dfs(i, set())):
                return False
        return True

            
            
