class Node:
    def __init__(self):
        self.next = [None] * 26
        self.wordEnd = False


def insertNode(head, word):
    temp = head

    for c in word:
        index = ord(c) - ord('a')
        if not temp.next[index]:
            temp.next[index] = Node()
        temp = temp.next[index]
    temp.wordEnd = True

def searchSentence(head, sentence):
    n = len(sentence)
    visited = [False] * (n + 1)
    visited[0] = True

    for i in range(n):
        if visited[i]:
            temp = head
            for j in range(i, n):
                if not temp:
                    break
                index = ord(sentence[j]) - ord('a')
                temp = temp.next[index]
                if temp and temp.wordEnd:
                    visited[j + 1] = True
    
    return visited[n]







if __name__ == '__main__':
    wordList = ["self", "th", "is", "famous", "word", "break", "b", "r", "e", "a", "k", "br", "bre", "brea", "ak", "prob", "lem"]
    sentence = "wordbreakproblem"

    head = Node()
    for word in wordList:
        insertNode(head, word)
    
    print(searchSentence(head, sentence))