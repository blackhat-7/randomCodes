from collections import defaultdict

def pairSumCount(arr, n):
    my_map = defaultdict(lambda: 0)
    total_pairs = 0
    for i in arr:
        total_pairs += my_map[n-i]
        my_map[i] += 1
    return total_pairs



arr = list(map(int, input().split()))
n = int(input())

print(pairSumCount(arr, n))
