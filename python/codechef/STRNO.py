import sys
from math import comb
def main():
    print(comb(1000000000, 1000000000//2))
    t = int(input())
    for q in range(t):
        x, k = map(int, input().split())
        numFactors = 0
        for i in range(k+1):
            numFactors += comb(k, i)
        if numFactors == x:
            sys.stdout.write("1\n")
        else:
            sys.stdout.write("0\n")

main()