
class MyTrie:

    def __init__(self):
        self.root = TrieNode()
    
    def charToIndex(self, ch):
        return ord(ch) - ord('a')

    def add(self, word):
        pCrawl = self.root
        length = len(word)
        for level in range(length):
            index = self.charToIndex(word[level])
            if not pCrawl.children[index]:
                pCrawl.children[index] = TrieNode()
            pCrawl = pCrawl.children[index]
        pCrawl.endOfWord = True
    
    def remove(self, word):
        pCrawl = self.root
        length = len(word)
        for level in range(length):
            index = self.charToIndex(word[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]
        if not pCrawl.endOfWord:
            return False
        pCrawl.endOfWord = False
        return True

    def search(self, word):
        pCrawl = self.root
        length = len(word)
        for level in range(length):
            index = self.charToIndex(word[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]
        return pCrawl.endOfWord


class TrieNode:
    ALPHABET_SIZE = 26
    def __init__(self):
        self.children = [None] * self.ALPHABET_SIZE
        self.endOfWord = False



if __name__ == '__main__':
    trie = MyTrie()
    words = ["example", "extempore", "exterminate"]
    for word in words:
        trie.add(word)
    print(trie.search("extempore"))
    print(trie.search("exterm"))