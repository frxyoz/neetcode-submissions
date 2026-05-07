class PrefixTree:

    def __init__(self):
       self.children = {} 
       self.end = False

    def insert(self, word: str) -> None:
        curr = self
        for i in range (len(word)):
            if word[i] not in curr.children.keys():
                curr.children[word[i]] = PrefixTree()
            curr = curr.children[word[i]]
        curr.end = True
        
            

    def search(self, word: str) -> bool:
        curr = self
        for i in range (len(word)):
            if word[i] not in curr.children.keys():
                return False
            curr = curr.children[word[i]]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for i in range (len(prefix)):
            if prefix[i] not in curr.children.keys():
                return False
            curr = curr.children[prefix[i]]
        return True
        