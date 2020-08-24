def main():
    t = int(input())
    for i in range(t):
        n, s, k = map(int, input().split())
        closed = list(map(int, input().split()))
        arr = [1]*(n+1)
        for i in closed:
            arr[i] = 0

        count = 0
        p = 0
        while(s-p > 0 or s+p < n+1):
            if s-p > 0 and arr[s-p] == 1:
                print(p)
                break
            elif s+p < n+1 and arr[s+p] == 1:
                print(p)
                break
            p += 1


main()
