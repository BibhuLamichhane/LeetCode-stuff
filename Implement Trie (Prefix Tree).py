class Trie:

    def __init__(self):
        self.vals = []

    def insert(self, word: str) -> None:
        self.vals.append(word)

    def search(self, word: str) -> bool:
        return word in self.vals

    def startsWith(self, prefix: str) -> bool:
        return any([prefix == i[0:len(prefix)] for i in self.vals])


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)