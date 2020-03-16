from collections import defaultdict

def occurance(L):

    d = defaultdict(int)
    for i in L:
        d[i] += 1
    result = max(d.items(), key=lambda x: x[1])[1]
    return result

n = int(input())

eggs = list(map(int, input().split()))
count = occurance(eggs)
if (n>1 and n<4 and n==count) or (n >= 4 and 2*count-n >= 2):
    print("No")
else:
    print("Yes")