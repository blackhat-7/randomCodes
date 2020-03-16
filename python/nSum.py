def main():
    x = int(input())
    lst = list(map(int, input().split()))
    recursiveSum(list(set(lst)), [], 0, x, 0)


def recursiveSum(lst, temp, s, x, c):
    if s == x:
        print(temp)
        return
    elif s > x:
        return
    
    for i in range(c, len(lst)):
        recursiveSum(lst, temp + [lst[i]], s+lst[i], x, i+1)


main()
