from math import gcd
from functools import reduce

def gcdList(list):
	return reduce(gcd, list)

t = int(input())
for i in range(t):
    n = int(input())
    seq = list(map(int, input().split()))
    seq = list(set(seq))
    n = len(seq)

    if n>=2 :
        seq1 = []
        seq2 = []

        max1 = max(seq[0],seq[1]) 
        max2 = min(seq[0],seq[1])
        maxIndex = seq.index(max1)
        max2Index = seq.index(max2)

        for i in range(2, n): 
            if seq[i]>max1: 
                max2=max1
                max2Index = maxIndex
                max1=seq[i] 
                maxIndex = i
            else: 
                if seq[i]>max2: 
                    max2=seq[i]
                    max2Index = i
        
        seq1 = seq[:maxIndex] + seq[maxIndex+1:]
        seq2 = seq[:max2Index] + seq[max2Index+1:]

        gcdsum1 = gcdList(seq1)+max1
        gcdsum2 = gcdList(seq2)+max2

        print(max(gcdsum1, gcdsum2))
    
    else:
        print(seq[0]*2)

        