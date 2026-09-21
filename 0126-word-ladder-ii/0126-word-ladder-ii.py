from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord, endWord, wordList):

        if endWord not in wordList:
            return []

        words = set(wordList)
        words.add(beginWord)

        
        patterns = defaultdict(list)

        for word in words:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                patterns[pattern].append(word)

        parent = defaultdict(list)

        queue = deque([beginWord])
        visited = {beginWord}
        found = False

        while queue and not found:

            level_visited = set()

            for _ in range(len(queue)):

                word = queue.popleft()

                for i in range(len(word)):

                    pattern = word[:i] + "*" + word[i + 1:]

                    for nxt in patterns[pattern]:

                        if nxt == word:
                            continue

                        
                        if nxt not in visited:

                            if nxt not in level_visited:
                                level_visited.add(nxt)
                                queue.append(nxt)

                            parent[nxt].append(word)

                        
                        elif nxt in level_visited:
                            parent[nxt].append(word)

                        if nxt == endWord:
                            found = True

            visited.update(level_visited)

        if endWord not in parent:
            return []

        
        result = []
        path = [endWord]

        def dfs(word):

            if word == beginWord:
                result.append(path[::-1])
                return

            for prev in parent[word]:
                path.append(prev)
                dfs(prev)
                path.pop()

        dfs(endWord)

        return result