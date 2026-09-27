class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # adjList of courses: prerequisites
        indeg = [0 for course in range(numCourses)]
        adjList = defaultdict(list)
        for a,b in prerequisites:
            adjList[b].append(a)
            indeg[a]+=1
        # start with 0 prereqs
        res = []

        # go through all courses
        queue = deque()
        # visited = set()

        for course in range(numCourses):
            # 0 indegree
            if indeg[course] == 0:
                queue.append(course)

                # visited.add(course)


        while(queue): 
            cur = queue.popleft()
            res.append(cur)

            for nei in adjList[cur]:
                indeg[nei] -=1

                if indeg[nei]==0: # add course if there are no indegrees       
                    queue.append(nei)
                    # visited.add(nei)


        return res if len(res) == numCourses else []

        # cycle case later
            


