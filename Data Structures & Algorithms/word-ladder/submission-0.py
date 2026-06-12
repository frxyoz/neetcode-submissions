class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        patterns_graph = defaultdict(list)

        for word in wordList + [beginWord]:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                patterns_graph[pattern].append(word)

        q = deque([(beginWord, 1)])
        visit = {beginWord}

        while q:
            curr_word, lvl = q.popleft()

            if curr_word == endWord:
                return lvl

            for i in range(len(curr_word)):
                pattern = curr_word[:i] + "*" + curr_word[i + 1:]

                for word in patterns_graph[pattern]:
                    if word not in visit:
                        visit.add(word)
                        q.append((word, lvl + 1))

        return 0