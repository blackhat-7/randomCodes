class Trie:
    class Node:
        def __init__(self):
            self.next = [None]*2

    def __init(self):
        self.root = Trie.Node()
    
    def insert(self, num):
        temp = self.root
        for i in range(32, -1, -1):
            index = num & (1 << i)
            if not temp.next[index]:
                temp.next[index] = Trie.Node()
            temp = temp.next[index]

#Optimal
def optimal(arr):
    trie = Trie()
    for num in arr:
        trie.insert(num)
    
    root = trie.root
    num1 = root
    num2 = root
    res = 0
    for i in range(32):
        if root.next[0] and root.next[1]:
            res = res | (1 << i)
        if root.next[0]:
            ansSet.add(root.next[0])
        if root.next[1]:
            ansSet.add(root.next[1])
    return res

#Optimal 2
def optimal2(arr):
    n = len(arr)
    mask = 0
    max_xor_res = 0

    for i in range(31, -1, -1):
        mask = mask | (1 << i)
        potential_max = max_xor_res | (1 << i)

        aset = set()
        for j in range(n):
            aset.add(arr[j] & mask)
        
        for a in aset:
            if a ^ potential_max in aset:
                max_xor_res = potential_max
                break
    print(max_xor_res)







#BruteForce
def bruteForce(arr):
    n = len(arr)
    maxXor = 0
    for i in range(n):
        for j in range(1+1, n):
            maxXor = max(maxXor, arr[i]^arr[j])
    print(maxXor)










if __name__ == '__main__':
    arr =  [25, 10, 2, 8, 5, 3]
    out = 28
    bruteForce(arr)
    optimal2(arr)