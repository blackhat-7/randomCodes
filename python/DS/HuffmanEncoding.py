from collections import Counter
import heapq
import pickle


class BinaryTree:
    class Node:
        def __init__(self, char, freq):
            self.left = None
            self.right = None
            self.char = str(char) if char is not None else None
            self.freq = freq

        def __lt__(self, other):
            return self.freq < other.freq

    def __init__(self):
        self.root = None
        self.encodedText = ''


class HuffmanEncoding:
    def __init__(self, text):
        self.text = text
        self.Bt = BinaryTree()
        self.code = {}
        self.encodedText = ''
        self.encode()

    def encode(self):
        self.buildTree()
        self.setCodes(self.Bt.root)
        self.encodeText()

    def decode(self):
        decodedText = ''
        node = self.Bt.root
        for bit in self.encodedText:
            if not node.left and not node.right:
                decodedText += node.char
                node = self.Bt.root
            if bit == '0':
                node = node.left
            elif bit == '1':
                node = node.right
        decodedText += node.char if not node.left and not node.right else ''
        print(decodedText)

    def encodeText(self):
        for ch in text:
            self.encodedText += self.code[ch]
        self.Bt.encodedText = bin(int(self.encodedText, 2))

    def setCodes(self, root, curr_code=''):
        if root != None:
            if root.char:
                self.code[root.char] = curr_code
            del root.freq
            self.setCodes(root.left, curr_code+'0')
            self.setCodes(root.right, curr_code+'1')

    def buildTree(self):
        count = Counter(text)
        pq = []
        for ch, freq in count.items():
            node = BinaryTree.Node(ch, freq)
            heapq.heappush(pq, node)
            self.code[ch] = ''

        while len(pq) > 1:
            node1, node2 = heapq.heappop(pq), heapq.heappop(pq)
            node3 = BinaryTree.Node(None, node1.freq + node2.freq)
            node3.left, node3.right = node1, node2
            heapq.heappush(pq, node3)
        self.Bt.root = pq[0]

    def saveEncodedTree(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.Bt, f)
            print('Saved encoded tree')


# text = "Huffman coding is a data compression algorithm..."
with open('text.txt', 'r') as f:
    text = f.read()

hc = HuffmanEncoding(text)
hc.decode()
hc.saveEncodedTree('textEncoded.txt')
