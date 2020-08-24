import sys
from math import comb
def main():
    t = int(input)
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