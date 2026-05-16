class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_index = -1  # -1 signifies that no word ends here initially

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word, index):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word_index = index 

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for i, word in enumerate(words):
            trie.insert(word, i)    
        out = []

        def dfs(node, x, y):
            if x < 0 or x > len(board)-1 or y < 0 or y > len(board[0]) - 1:
                return
            #  current board char
            temp = board[x][y]
            # if char not in node.children, return
            if temp not in node.children:
                return
            # move into trie child
            node = node.children[temp]
            # if trie node forms a word:
            if node.word_index != -1:
                out.append(words[node.word_index])
                node.word_index = -1 

            # mark visited
            board[x][y] = '#'
            # explore 4 directions
            dfs(node, x+1, y)
            dfs(node, x-1, y)
            dfs(node, x, y-1)
            dfs(node, x, y+1)
            # unmark visited
            board[x][y] = temp
            


        # ... (Run your DFS board traversal here) ...
        for x in range(len(board)):
            for y in range(len(board[0])):
                dfs(trie.root, x, y)


        return out