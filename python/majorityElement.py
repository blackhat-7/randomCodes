def findMajority(arr, n, low, high):
    if n != 1:
        mid = low + (high-low)//2  
        findMajority(arr, n//2, low, mid)
        findMajority(arr, n//2, mid, high)

def main():
    arr = list(map(int, input().split()))
    n = len(arr)
    findMajority(arr, n)