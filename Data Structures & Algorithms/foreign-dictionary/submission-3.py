class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # finding similarities to move it up
        # make r relationship on differences pop on differences
        # add r to graph; a->b
        # indegrees[a] = indegrees.get(a,0)
        # indegree[b]+= indegrees.get(b,0) +1

        # or  one of words get to the end;  
            # go to next word
        # prev = cur; next word
        # start back at 0
        # order = ""
        # graph = {n: [f], h:[e] r: [n] e:[f]} 
        # rnhef
        # prev = nn
        # cur  = fnn
        order = []
        if len(words) == 1:
            return words[0]
        graph = defaultdict(list)

        prev = words[0]
        indegree = {}
        end = set()
        for i in range(1,len(words)):
            cur = words[i]
            j=0
            # ends whoeever word runs out first
            while(j < len(cur) and j < len(prev)):
                a, b = prev[j], cur[j]
                if a == b:
                    if a not in indegree and a not in end:
                        end.add(a)
                    if b not in indegree and b not in end:
                        end.add(a)
                    j+=1
                else:
                    # relationship a -> b
                    if a in end:
                        end.remove(a)
                    if b in end:
                        end.remove(b)
                    graph[a].append(b)
                    indegree[a] = indegree.get(a,0)
                    indegree[b] = indegree.get(b,0) +1
                    break
            # process rest of letters not accounted for at the end
            # state or prev and cur: different or end of word 
            cur_j = j
            prev_j = j
            if cur_j == len(cur) and prev_j < len(prev):
                return ""


            while(prev_j<len(prev)):
                c= prev[prev_j]
                if c not in indegree and c not in end:
                    end.add(c)
                prev_j+=1
            while(cur_j<len(cur)):
                c = cur[cur_j]
                if c not in indegree and c not in end:
                    end.add(c)
                cur_j+=1

            # print(prev, cur, end)

            prev = cur
        print(graph)

    
        q=[]
        # kahns count indegrees
        for k,v in indegree.items():
            if v == 0:
                q.append(k)        

        while(q):
            cur = q.pop()
            order.append(cur)


            for child in graph[cur]:
                indegree[child] -=1
                if indegree[child] == 0:
                    q.append(child)

        if len(order) < len(indegree):
            print("cycle")
            return ""

        order.extend(list(end))
        # print(order)

        return "".join(order)

            # c->b    a-> bc

            # a->b,c    c->b
        
# ["abc","bcd","cde"]
# a->b b->c 

# process res of letters that didnt make it

        



