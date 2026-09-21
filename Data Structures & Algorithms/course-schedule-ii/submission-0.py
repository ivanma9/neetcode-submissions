class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hm = {}
        indegree = [0] * numCourses
        for c,p in prerequisites:
            if c not in hm:
                hm[c] = []
            indegree[p] += 1
            hm[c].append(p)



        queue = []
        output = []

        for i in range(numCourses):
            if i not in hm:
                hm[i] = []
            if indegree[i] == 0:
                queue.append(i)

                # top nodes, last class

        while(queue):
            cur = queue.pop(0)
            output.append(cur)

            for c in hm[cur]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    queue.append(c)


        if len(output) != numCourses:
            return []
        return output[::-1]
                


            
