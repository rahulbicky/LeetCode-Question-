class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        queue = deque()
        queue.append((beginWord,1))
        while len(queue)!=0:
            curr_word,level=queue.popleft()
            if curr_word == endWord:
                return level
            for i in range(0,len(curr_word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    if ch == curr_word[i]:
                        continue
                    new_word = curr_word[:i]+ ch + curr_word[i+1:]
                    if new_word in wordSet:
                        queue.append((new_word,level+1))
                        wordSet.remove(new_word)
        return 0
