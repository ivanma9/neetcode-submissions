class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = defaultdict(list)

        def word_to_graph(w):
            for i in range(len(w)):
                star_w = w[:i] + "*" + w[i + 1:]
                graph[w].append(star_w)
                graph[star_w].append(w)
        for w in wordList:
            word_to_graph(w)
        
        word_to_graph(beginWord)

        #dfs 
        # print(graph)
        visited = set()
        q = deque()
        q.append((beginWord, 1))
        while(q):
            cur, step = q.popleft()
            if cur == endWord:
                return step // 2 + 1
            for child in graph[cur]:
                if child in visited:
                    continue
                visited.add(child)
                q.append((child, step+1))
        return 0


        # def dfs(word, dist):
        #     # print(word,dist, visited)
        #     if word == endWord:
        #         print("fini")
        #         return dist
        #     visited.add(word)
        #     ans = float('inf')
        #     for child in graph[word]:
        #         if child in visited:
        #             continue
        #         # print(child, dist)
        #         ans = min(ans, dfs(child, dist+1))
        #     visited.remove(word)
        #     return ans

        # res = dfs(beginWord, 0)
        # return (res // 2) + 1 if res != float('inf') else 0
                

                 
